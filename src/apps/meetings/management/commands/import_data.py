import re
import glob
from openpyxl import load_workbook
from dateutil.parser import parse
from django.conf import settings
from django.core.management.base import BaseCommand

from apps.meetings.domain.enums import AuthorClassification, MeetingType, Solution
from apps.meetings.models import Meeting, Question, Tag


COLUMN_ORDER = [
    'year',
    'month',
    'day',
    'protocol_number',
    'meeting_type',
    'deputies',
    'presiding',
    'quorum',
    'position_1870',
    'position_1892',
    'author_classification',
    'number',
    'description',
    'tags',
    'solution',
    'solution_content',
    'case_number',
    'sheet_numbers',
]

month_map = {
    'январь': 'Jan', 'февраль': 'Feb', 'март': 'Mar', 'апрель': 'Apr',
    'май': 'May', 'июнь': 'Jun', 'июль': 'Jul', 'август': 'Aug',
    'сентябрь': 'Sep', 'октябрь': 'Oct', 'ноябрь': 'Nov', 'декабрь': 'Dec'
}


class Command(BaseCommand):
    help = 'Мигрирует данные из Excel файлов'

    def get_columns(self, rows):
        header_row = [column for column in next(rows) if column is not None]
        if len(header_row) == 19:
            is_old = True
        elif len(header_row) == 18:
            is_old = False
        else:
            self.stdout.write(self.style.ERROR('Ошибка: неизвестная структура документа'))
            return

        columns = {}
        for idx, column in enumerate(header_row):
            if idx > 11 and is_old:
                columns[COLUMN_ORDER[idx - 1]] = idx
            else:
                columns[COLUMN_ORDER[idx]] = idx

        return columns

    def handle(self, *args, **options):
        files = glob.glob(f'{settings.DATA_PATH}/*.xlsx')
        for file in files:
            workbook = load_workbook(file, read_only=True)
            first_sheet = workbook.sheetnames[0]
            sheet = workbook[first_sheet]

            rows = sheet.values
            columns = self.get_columns(rows)
            if columns is None:
                continue

            total_rows = 0
            imported_rows = 0
            
            actual_meeting = None
            for idx, row in enumerate(rows):
                if not any(value is not None for value in row):
                    break

                total_rows += 1

                try:
                    date = parse(f'{row[columns['year']]} {month_map[row[columns['month']].lower().strip()]} {row[columns['day']]}').date()
                    meeting_type = MeetingType.get_value_by_label(row[columns['meeting_type']].split()[0].strip())
                    deputies = int(row[columns['deputies']])
                    presiding = row[columns['presiding']]

                    if actual_meeting is None or actual_meeting.date != date:
                        new_meeting = Meeting.objects.create(
                            date=date,
                            meeting_type=meeting_type,
                            deputies=deputies,
                            presiding=presiding
                        )
                        actual_meeting = new_meeting

                    meeting = actual_meeting.id
                    protocol_number = row[columns['protocol_number']] or ''
                    number = row[columns['number']] or ''
                    description = row[columns['description']] or ''
                    quorum = True if row[columns['quorum']].lower() == 'да' else False
                    position_1870 = row[columns['position_1870']][:1].capitalize() if row[columns['position_1870']] else ''
                    position_1892 = row[columns['position_1892']] if row[columns['position_1892']] else ''
                    author_classification = AuthorClassification.get_value_by_label(row[columns['author_classification']].strip())
                    solution = Solution.get_value_by_label(row[columns['solution']].strip()) if row[columns['solution']] else ''
                    solution_content = row[columns['solution_content']] or ''
                    case_number = row[columns['case_number']] or ''
                    tags = row[columns['tags']] or ''

                    sheet_numbers = str(row[columns['sheet_numbers']]).split('-')
                    sheet_numbers_list = []

                    for part in sheet_numbers:
                        part = part.strip().replace(' ', '').replace('.', '')
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

                    for tag in re.split(r'[;,]+', tags):
                        cleaned_tag = tag.strip()
                        if cleaned_tag:
                            cleaned_tag = f'{cleaned_tag[0].capitalize()}{cleaned_tag[1:] if len(cleaned_tag) > 1 else ''}'
                            new_tag = Tag.objects.get_or_create(title=cleaned_tag)[0]
                            new_question.tags.add(new_tag)

                    imported_rows += 1

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Не удалось обработать строку {idx + 2} в файле "{file}": {e}'))

            self.stdout.write(self.style.SUCCESS(f'{file}: {imported_rows}/{total_rows}'))
