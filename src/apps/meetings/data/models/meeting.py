from django.db import models
from apps.meetings.domain.enums import MeetingType, Month


class Meeting(models.Model):
    date = models.DateField(verbose_name='Дата заседания')
    protocol_number = models.CharField(max_length=8, verbose_name='№ протокола')
    meeting_type = models.CharField(max_length=16, choices=MeetingType, verbose_name='Тип заседания')
    deputies = models.IntegerField(verbose_name='Число гласных')
    presiding = models.CharField(max_length=64, verbose_name='Председательствующий')

    class Meta:
        verbose_name = 'заседание'
        verbose_name_plural = 'Заседания'

    def __str__(self):
        return f'{self.get_meeting_type_display()} заседание ({self.date})'
