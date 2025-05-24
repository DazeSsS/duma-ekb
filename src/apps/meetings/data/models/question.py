from django.db import models
from django.contrib.postgres.fields import ArrayField
from apps.meetings.domain.enums import (
    AuthorClassification,
    Position1870,
    Position1892,
    Solution,
)


class Question(models.Model):
    meeting = models.ForeignKey('Meeting', on_delete=models.CASCADE, related_name='questions', verbose_name='Заседание')
    protocol_number = models.CharField(max_length=8, db_index=True, verbose_name='№ протокола')
    number = models.CharField(max_length=8, blank=True, verbose_name='№ вопроса')
    description = models.TextField(max_length=1024, verbose_name='Решаемый вопрос')
    quorum = models.BooleanField(verbose_name='Кворум')
    position_1870 = models.CharField(max_length=2, choices=Position1870, blank=True, verbose_name='Положение 1870')
    position_1892 = models.CharField(max_length=5, choices=Position1892, blank=True, verbose_name='Положение 1892')
    author_classification = models.CharField(max_length=16, choices=AuthorClassification, blank=True, db_index=True, verbose_name='Авторская классификация')
    solution = models.CharField(max_length=16, choices=Solution, blank=True, verbose_name='Решение')
    solution_content = models.TextField(max_length=1024, blank=True, verbose_name='Содержание решения')
    case_number = models.CharField(max_length=8, db_index=True, verbose_name='№ дела')
    sheet_numbers = ArrayField(models.CharField(max_length=16), verbose_name='Номера листов')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='Ключевые слова')

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['number']

    def __str__(self):
        return f'{self.number}. {self.description}'
