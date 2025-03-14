from django.db import models
from django.contrib.postgres.fields import ArrayField


class Question(models.Model):
    class Solution(models.TextChoices):
        AGREE = 'agree', 'Согласны'
        PUT_OFF = 'put_off', 'Отложить'
        REFUSE = 'refuse', 'Отказать'
        TAKE_NOTE = 'take_note', 'Принять к сведению'

    number = models.IntegerField()
    description = models.CharField()
    solution = models.CharField(choices=Solution)
    solution_content = models.CharField()
    case_number = models.CharField()
    sheet_numbers = ArrayField(models.DecimalField(max_digits=5, decimal_places=1))

    def __str__(self):
        return f'{self.number}. {self.description[:40]}...'
