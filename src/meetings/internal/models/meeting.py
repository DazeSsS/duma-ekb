from django.db import models
from meetings.enums import AuthorClassification, MeetingType, Month, Position1870, Position1892


class Meeting(models.Model):
    year = models.IntegerField()
    month = models.CharField(choices=Month)
    day = models.IntegerField()
    protocol_number = models.IntegerField()
    meeting_type = models.CharField(choices=MeetingType)
    # deputies = models.ManyToManyField()
    presiding = models.CharField()
    quorum = models.BooleanField()
    position_1870 = models.CharField(choices=Position1870)
    position_1892 = models.CharField(choices=Position1892)
    tag = models.ManyToManyField('Tag')
    author_classification = models.CharField(choices=AuthorClassification)
    author_classification_2 = models.CharField(choices=AuthorClassification)
    # question = models.ForeignKey('Question', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.day} {self.month} {self.year} {self.meeting_type}'
