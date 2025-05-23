from django.db import models
from django.contrib import admin
from django_flatpickr.settings import FlatpickrOptions
from django_flatpickr.widgets import DatePickerInput

from apps.meetings.data.models import Meeting
from apps.meetings.data.admin.question import QuestionInline


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'meeting_type', 'deputies', 'presiding']
    inlines = [QuestionInline]
    fields = [
        'date',
        'meeting_type',
        'deputies',
        'presiding',
    ]
    ordering = ['-date']

    formfield_overrides = {
        models.DateField: {'widget': DatePickerInput(
            options=FlatpickrOptions(
                altFormat='d F Y',
                allowInput=True,
                locale='ru',
            )
        )},
    }
