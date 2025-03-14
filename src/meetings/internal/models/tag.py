from django.db import models


class Tag(models.Model):
    title = models.CharField()

    def __str__(self):
        return self.title
