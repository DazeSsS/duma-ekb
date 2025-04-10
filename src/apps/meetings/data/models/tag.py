from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=32, verbose_name='Заголовок')

    class Meta:
        verbose_name = 'ключевое слово'
        verbose_name_plural = 'Ключевые слова'
        ordering = ['title']

    def __str__(self):
        return self.title
