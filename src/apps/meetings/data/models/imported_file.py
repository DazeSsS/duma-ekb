from django.db import models


class ImportedFile(models.Model):
    filename = models.CharField(max_length=128, unique=True, verbose_name='Имя файла')
    errors = models.TextField(verbose_name='Ошибки импорта')

    class Meta:
        verbose_name = 'импортированный файл'
        verbose_name_plural = 'Импортированные файлы'

    def __str__(self):
        return self.filename
