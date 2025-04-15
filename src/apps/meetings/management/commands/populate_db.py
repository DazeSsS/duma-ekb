from datetime import date
from django.core.management.base import BaseCommand

from apps.meetings.data.models import Meeting, Tag, Question
from apps.meetings.domain.enums import (
    AuthorClassification,
    MeetingType,
    Position1870,
    Position1892,
    Solution,
)


class Command(BaseCommand):
    help = 'Заполняет базу данных моковыми данными'

    def handle(self, *args, **options):
        # Создание ключевых слов
        elections_tag = Tag.objects.get_or_create(title='Выборы')[0]
        law_tag = Tag.objects.get_or_create(title='Охрана правопорядка')[0]
        complaint_tag = Tag.objects.get_or_create(title='Жалоба')[0]
        paduchev_tag = Tag.objects.get_or_create(title='В.А. Падучев')[0]
        muslim_tag = Tag.objects.get_or_create(title='Мусульмане')[0]
        conflict_tag = Tag.objects.get_or_create(title='Конфликт')[0]
        taxes_tag = Tag.objects.get_or_create(title='Налоги')[0]


        # Заседание 9 Января 1906
        meeting_1906_01_09 = Meeting.objects.create(
            date=date(1906, 1, 9),
            protocol_number='1',
            meeting_type=MeetingType.EMERGENCY,
            deputies=22,
            presiding='Анфиногенов И.К.',
        )

        Question.objects.create(
            meeting=meeting_1906_01_09,
            number='1',
            description='Избрание комиссии для составления списка избирателей для выборов в Государственную думу',
            quorum=True,
            position_1870=Position1870.A,
            position_1892=Position1892.XII,
            author_classification=AuthorClassification.CITY_GOVERNMENT,
            solution=Solution.AGREE,
            solution_content='',
            case_number='1982',
            sheet_numbers=[2, 3.5]
        ).tags.add(elections_tag)


        # Заседание 18 января 1906
        meeting_1906_01_18 = Meeting.objects.create(
            date=date(1906, 1, 18),
            protocol_number='2',
            meeting_type=MeetingType.REGULAR,
            deputies=29,
            presiding='Анфиногенов И.К.',
        )

        Question.objects.create(
            meeting=meeting_1906_01_18,
            number='1',
            description='Жалоба на отмену решения городской думы об учреждении конной стражи за счет городского бюджета',
            quorum=True,
            position_1870=Position1870.A,
            position_1892=Position1892.XII,
            author_classification=AuthorClassification.CITY_GOVERNMENT,
            solution=Solution.AGREE,
            solution_content='Обжаловать в Сенате',
            case_number='1982',
            sheet_numbers=[10, 11.5]
        ).tags.add(law_tag)

        Question.objects.create(
            meeting=meeting_1906_01_18,
            number='2',
            description='Жалоба на отмену решения думы об извещении Синода о проповеди',
            quorum=True,
            position_1870=Position1870.A,
            position_1892=Position1892.XII,
            author_classification=AuthorClassification.CITY_GOVERNMENT,
            solution=Solution.AGREE,
            solution_content='Обжаловать в Сенате',
            case_number='1982',
            sheet_numbers=[11.5, 13]
        ).tags.add(complaint_tag)

        Question.objects.create(
            meeting=meeting_1906_01_18,
            number='3',
            description='Жалоба на отмену решения городской думы об учреждении и организации городской милиции',
            quorum=True,
            position_1870=Position1870.A,
            position_1892=Position1892.XII,
            author_classification=AuthorClassification.CITY_GOVERNMENT,
            solution=Solution.AGREE,
            solution_content='Обжаловать в Сенате',
            case_number='1982',
            sheet_numbers=[13, 14.5]
        ).tags.add(complaint_tag)

        Question.objects.create(
            meeting=meeting_1906_01_18,
            number='4',
            description='Выборы представителей думы в педагогические советы среднеобразовательных учебных заведений',
            quorum=True,
            position_1870=Position1870.A,
            position_1892=Position1892.XII,
            author_classification=AuthorClassification.CITY_GOVERNMENT,
            solution=Solution.AGREE,
            solution_content='',
            case_number='1982',
            sheet_numbers=[14.5, 15]
        ).tags.add(elections_tag)

        Question.objects.create(
            meeting=meeting_1906_01_18,
            number='5',
            description='Жалоба больных венерологического отделения',
            quorum=True,
            position_1870=Position1870.D,
            position_1892=Position1892.VI,
            author_classification=AuthorClassification.HEALTH_CARE,
            solution=Solution.PUT_OFF,
            solution_content='Создать комиссию',
            case_number='1982',
            sheet_numbers=[15, 25]
        ).tags.add(paduchev_tag)


        # Заседание 20 января 1906 
        meeting_1906_01_20 = Meeting.objects.create(
            date=date(1906, 1, 20),
            protocol_number='2',
            meeting_type=MeetingType.ONGOING,
            deputies=25,
            presiding='Анфиногенов И.К.',
        )

        Question.objects.create(
            meeting=meeting_1906_01_20,
            number='6',
            description='Ходатойство купцов-мусульман о разрешении торговли в воскресенье',
            quorum=True,
            position_1870=Position1870.C,
            position_1892=Position1892.VI,
            author_classification=AuthorClassification.TRADING,
            solution=Solution.REFUSE,
            solution_content='',
            case_number='1982',
            sheet_numbers=[25.5, 28]
        ).tags.add(muslim_tag)

        Question.objects.create(
            meeting=meeting_1906_01_20,
            number='7',
            description='Результаты расследования пожарной комиссии о жалобе А.П. Кожевникова на содержание брандмейстером Чапиным собственных лошадей за счет пожарного ведомства',
            quorum=True,
            position_1870=Position1870.A,
            position_1892=Position1892.XII,
            author_classification=AuthorClassification.CITY_GOVERNMENT,
            solution=Solution.TAKE_NOTE,
            solution_content='Не подтвердилось',
            case_number='1982',
            sheet_numbers=[28, 33]
        ).tags.add(conflict_tag)

        Question.objects.create(
            meeting=meeting_1906_01_20,
            number='8',
            description='Возложение на Управу оценки городских недвижимых имуществ',
            quorum=True,
            position_1870=Position1870.A,
            position_1892=Position1892.I,
            author_classification=AuthorClassification.FINANCE,
            solution=Solution.AGREE,
            solution_content='',
            case_number='1982',
            sheet_numbers=[33, 33.5]
        ).tags.add(taxes_tag)

        self.stdout.write(self.style.SUCCESS('Тестовые данные загружены!'))
