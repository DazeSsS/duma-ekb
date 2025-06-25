from typing import Literal
from datetime import date

from django.core.paginator import Paginator
from django.db.models.functions import Length
from django.db.models import Q, Prefetch
from ninja import Router, Query

from apps.meetings.data.models import Meeting, Question
from apps.meetings.domain.enums import AuthorClassification
from apps.meetings.domain.schemas import MeetingResponse, PaginatedResponse
from apps.meetings.api.responses import NotFoundResponse


router = Router(
    tags=['Meetings'],
    by_alias=True,
)


@router.get('/', response={200: PaginatedResponse[MeetingResponse]})
def list_meetings(
    request,
    date: date | None = Query(None),
    date_from: date | None = Query(None),
    date_to: date | None = Query(None),
    year: int | None = Query(None),
    month: int | None = Query(None),
    presiding: str | None = Query(None),
    classification: Literal[*AuthorClassification.values] | None = Query(None),
    case: str | None = Query(None),
    protocol: str | None = Query(None),
    question_number: str | None = Query(None),
    tags: str | None = Query(None),
    page: int = 1,
    per_page: int = 10
):
    meetings = Meeting.objects.all().order_by('date')

    question_filters = Q()

    if tags:
        question_filters &= Q(tags__title__icontains=tags)
    if classification:
        question_filters &= Q(author_classification=classification)
    if case:
        question_filters &= Q(meeting__case_number=case)
        if protocol:
            question_filters &= Q(meeting__protocol_number=protocol)
            if question_number:
                question_filters &= Q(number=question_number)

    questions_prefetch = Prefetch(
        'questions',
        queryset=(
            Question.objects
            .filter(question_filters)
            .distinct()
            .order_by(Length('number'), 'number')
        ),
        to_attr='filtered_questions'
    )

    if date:
        meetings = meetings.filter(date=date)
    elif date_from and date_to:
        meetings = meetings.filter(date__range=(date_from, date_to))
    elif date_from:
        meetings = meetings.filter(date__gte=date_from)
    elif date_to:
        meetings = meetings.filter(date__lte=date_to)
    elif year and month:
        meetings = meetings.filter(date__year=year, date__month=month)
    elif year:
        meetings = meetings.filter(date__year=year)

    if presiding:
        meetings = meetings.filter(presiding__icontains=presiding)

    meetings = meetings.prefetch_related(questions_prefetch).filter(
        questions__in=Question.objects.filter(question_filters)
    ).distinct()

    paginator = Paginator(meetings, per_page)
    page_obj = paginator.get_page(page)

    meetings_list = list(page_obj.object_list)
    for meeting in meetings_list:
        meeting.questions.set(meeting.filtered_questions) 
    
    return PaginatedResponse[MeetingResponse](
        items=meetings_list,
        total_pages=paginator.num_pages,
        current_page=page_obj.number
    )


@router.get('/presidings/', response={200: PaginatedResponse[str]})
def list_presidings(
    request,
    page: int = 1,
    per_page: int = 10
):
    presidings = (
        Meeting.objects
        .values_list('presiding', flat=True)
        .distinct()
        .order_by('presiding')
    )

    paginator = Paginator(presidings, per_page)
    page_obj = paginator.get_page(page)

    presidings_list = list(page_obj.object_list)

    return PaginatedResponse[str](
        items=presidings_list,
        total_pages=paginator.num_pages,
        current_page=page_obj.number
    )


@router.get('/case-numbers/', response={200: PaginatedResponse[str]})
def list_case_numbers(
    request,
    page: int = 1,
    per_page: int = 10
):
    case_numbers = (
        Meeting.objects
        .values_list('case_number', flat=True)
        .distinct()
        .order_by('case_number')
    )

    paginator = Paginator(case_numbers, per_page)
    page_obj = paginator.get_page(page)

    case_numbers_list = list(page_obj.object_list)

    return PaginatedResponse[str](
        items=case_numbers_list,
        total_pages=paginator.num_pages,
        current_page=page_obj.number
    )


@router.get('/protocol-numbers/', response={200: PaginatedResponse[str]})
def list_protocol_numbers(
    request,
    case_number: str,
    page: int = 1,
    per_page: int = 10
):
    protocol_numbers = (
        Meeting.objects
        .filter(case_number=case_number)
        .values_list('protocol_number', flat=True)
        .distinct()
        .order_by(Length('protocol_number'), 'protocol_number')
    )

    paginator = Paginator(protocol_numbers, per_page)
    page_obj = paginator.get_page(page)

    protocol_numbers_list = list(page_obj.object_list)

    return PaginatedResponse[str](
        items=protocol_numbers_list,
        total_pages=paginator.num_pages,
        current_page=page_obj.number
    )


@router.get('/question-numbers/', response={200: PaginatedResponse[str]})
def list_question_numbers(
    request,
    case_number: str,
    protocol_number: str,
    page: int = 1,
    per_page: int = 10
):
    question_numbers = (
        Question.objects
        .filter(meeting__case_number=case_number, meeting__protocol_number=protocol_number)
        .values_list('number', flat=True)
        .distinct()
        .order_by(Length('number'), 'number')
    )

    paginator = Paginator(question_numbers, per_page)
    page_obj = paginator.get_page(page)

    question_numbers_list = list(page_obj.object_list)

    return PaginatedResponse[str](
        items=question_numbers_list,
        total_pages=paginator.num_pages,
        current_page=page_obj.number
    )


@router.get('/{id}/', response={200: MeetingResponse, 404: NotFoundResponse})
def get_meeting_by_id(request, id: int):
    meeting = Meeting.objects.get(id=id)
    return meeting
