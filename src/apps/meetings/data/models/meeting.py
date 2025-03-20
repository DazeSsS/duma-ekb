from django.db import models
from apps.meetings.domain.enums import (
    AuthorClassification,
    MeetingType,
    Month,
    Position1870,
    Position1892,
)


class Meeting(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=16, choices=Month)
    day = models.IntegerField()
    protocol_number = models.IntegerField()
    meeting_type = models.CharField(max_length=16, choices=MeetingType)
    deputies = models.IntegerField()
    presiding = models.CharField(max_length=64)
    quorum = models.BooleanField()
    position_1870 = models.CharField(max_length=2, choices=Position1870)
    position_1892 = models.CharField(max_length=5, choices=Position1892)
    tag = models.ManyToManyField('Tag')
    author_classification = models.CharField(max_length=16, choices=AuthorClassification)
    author_classification_2 = models.CharField(max_length=16, choices=AuthorClassification, null=True, blank=True)

    def __str__(self):
        return f'{self.day} {self.get_month_display()} {self.year}'
