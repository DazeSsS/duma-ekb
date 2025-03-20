from django.db import models
from django.contrib.postgres.fields import ArrayField
from apps.meetings.domain.enums import Solution


class Question(models.Model):
    meeting = models.ForeignKey('Meeting', on_delete=models.CASCADE)
    number = models.CharField(max_length=8)
    description = models.TextField(max_length=1024)
    solution = models.CharField(max_length=16, choices=Solution)
    solution_content = models.TextField(max_length=1024, blank=True)
    case_number = models.CharField(max_length=8)
    sheet_numbers = ArrayField(models.DecimalField(max_digits=5, decimal_places=1))

    def __str__(self):
        return f'{self.number}. {self.description}'
