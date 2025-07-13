import glob
from pathlib import Path
from django.conf import settings
from django.core.management.base import BaseCommand

from utils.meetings_parser import import_file, OnCollision
from apps.meetings.exceptions import InvalidDocumentStructure
from apps.meetings.models import ImportedFile


class Command(BaseCommand):
    help = 'Мигрирует данные из Excel файлов'

    def handle(self, *args, **options):
        files = [Path(file) for file in glob.glob(f'{settings.DATA_PATH}/*.xlsx')]
        imported_files = ImportedFile.objects.values_list('filename', flat=True)

        on_collision = None
        for file in files:
            if file.name in imported_files:
                while on_collision not in [OnCollision.REPLACE.value, OnCollision.SKIP.value]:
                    on_collision = int(input(
                        'Что вы хотите сделать с уже импортированными файлами?\n'
                        '1) Перезаписать данные из этих файлов\n'
                        '2) Пропустить\n'
                        '>> '
                    ))
                break

        for file in files:
            try:
                message_generator = import_file(file, on_collision)

                new_message = next(message_generator)
                while new_message:
                    if new_message.startswith('SUCCESS:'):
                        self.stdout.write(self.style.SUCCESS(new_message))
                    elif new_message.startswith('ERROR:'):
                        self.stdout.write(self.style.ERROR(new_message))
                    new_message = next(message_generator, None)

            except InvalidDocumentStructure as e:
                self.stdout.write(self.style.ERROR(e))
