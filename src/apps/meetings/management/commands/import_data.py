from openpyxl import load_workbook
from dateutil.parser import parse
from django.conf import settings
from django.core.management.base import BaseCommand

from apps.meetings.domain.enums import AuthorClassification, MeetingType, Solution
from apps.meetings.models import Meeting, Question, Tag


TABLE_HEADERS = {
    'Год': 0,
    'Месяц': 1,
    'День': 2,
    '№ протокола': 3,
    'заседание': 4,
    'Число гласных': 5,
    'Председательствующий': 6,
    'Кворум': 7,
    'Положение 1870': 8,
    'Положение 1892': 9,
    'Авторская классификация': 10,
    '№ вопроса': 12,
    'Решаемый вопрос': 13,
    'Ключевые слова': 14,
    'Решение': 15,
    'Содержание решения': 16,
    '№ дела': 17,
    '№№ листов': 18,
}

month_map = {
    'январь': 'Jan', 'февраль': 'Feb', 'март': 'Mar', 'апрель': 'Apr',
    'май': 'May', 'июнь': 'Jun', 'июль': 'Jul', 'август': 'Aug',
    'сентябрь': 'Sep', 'октябрь': 'Oct', 'ноябрь': 'Nov', 'декабрь': 'Dec'
}


class Command(BaseCommand):
    help = 'Мигрирует данные из Excel файлов'

    def handle(self, *args, **options):
        workbook = load_workbook(settings.DATA_PATH / '1906_1.xlsx', read_only=True)
        first_sheet = workbook.sheetnames[0]
        sheet = workbook[first_sheet]

        rows = sheet.values
        header_row = next(rows)
        if len(header_row) == 19:
            pass

        for row in rows:
            if not any(value is not None for value in row):
                break

            actual_meeting = None

            date = parse(f'{row[0]} {month_map[row[1].lower()]} {row[2]}').date()
            meeting_type = MeetingType.get_value_by_label(row[4])
            deputies = int(row[5])
            presiding = row[6]

            if not actual_meeting or actual_meeting.date != date:
                new_meeting = Meeting.objects.create(
                    date=date,
                    meeting_type=meeting_type,
                    deputies=deputies,
                    presiding=presiding
                )
                actual_meeting = new_meeting
            

            meeting = actual_meeting.id
            protocol_number = row[3] or ''
            number = row[12] or ''
            description = row[13] or ''
            quorum = True if row[7].lower() == 'да' else False
            position_1870 = row[8].capitalize() if row[8] else ''
            position_1892 = row[9] if row[9] else ''
            author_classification = AuthorClassification.get_value_by_label(row[10])
            solution = Solution.get_value_by_label(row[15]) if row[15] else ''
            solution_content = row[16] or ''
            case_number = row[17] or ''
            tags = row[14] or ''

            sheet_numbers = str(row[18]).split('-')
            sheet_numbers_list = []

            for part in sheet_numbers:
                part = part.strip().replace(' ', '')
                if 'об' in part:
                    num = float(part.replace('об', '.5'))
                else:
                    num = float(part)

                sheet_numbers_list.append(num)

            if len(sheet_numbers_list) == 1:
                sheet_numbers_list.append(sheet_numbers_list[0])

            new_question = Question.objects.create(
                meeting_id=meeting,
                protocol_number=protocol_number,
                number=number,
                description=description,
                quorum=quorum,
                position_1870=position_1870,
                position_1892=position_1892,
                author_classification=author_classification,
                solution=solution,
                solution_content=solution_content,
                case_number=case_number,
                sheet_numbers=sheet_numbers_list,
            )

            for tag in tags.split(','):
                if tag:
                    cleaned_tag = tag.strip()
                    cleaned_tag = cleaned_tag[0].capitalize() + cleaned_tag[1:]
                    new_tag = Tag.objects.get_or_create(title=cleaned_tag)[0]
                    new_question.tags.add(new_tag)
