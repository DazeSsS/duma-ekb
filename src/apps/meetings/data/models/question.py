from django.db import models
from django.contrib.postgres.fields import ArrayField
from apps.meetings.domain.enums import (
    AuthorClassification,
    Position1870,
    Position1892,
    Solution,
)


class Question(models.Model):
    meeting = models.ForeignKey('Meeting', on_delete=models.CASCADE, verbose_name='Заседание')
    number = models.CharField(max_length=8, verbose_name='№ вопроса', blank=True)
    description = models.TextField(max_length=1024, verbose_name='Решаемый вопрос')
    quorum = models.BooleanField(verbose_name='Кворум')
    position_1870 = models.CharField(max_length=2, choices=Position1870, verbose_name='Положение 1870')
    position_1892 = models.CharField(max_length=5, choices=Position1892, verbose_name='Положение 1892')
    author_classification = models.CharField(max_length=16, choices=AuthorClassification, verbose_name='Авторская классификация')
    solution = models.CharField(max_length=16, choices=Solution, verbose_name='Решение')
    solution_content = models.TextField(max_length=1024, blank=True, verbose_name='Содержание решения')
    case_number = models.CharField(max_length=8, verbose_name='№ дела')
    sheet_numbers = ArrayField(models.DecimalField(max_digits=5, decimal_places=1), verbose_name='Номера листов')
    tags = models.ManyToManyField('Tag', verbose_name='Ключевые слова')

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f'{self.number} {self.description}'
