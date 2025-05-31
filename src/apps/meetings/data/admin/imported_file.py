from django.contrib import admin

from apps.meetings.data.models import ImportedFile


@admin.register(ImportedFile)
class ImportedFileAdmin(admin.ModelAdmin):
    pass
