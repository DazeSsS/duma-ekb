from django.contrib import admin
from django.conf import settings

from apps.meetings.data.admin import (
    ImportedFileAdmin,
    MeetingAdmin,
    QuestionAdmin,
    TagAdmin,
)


admin.site.site_header = settings.SITE_HEADER
admin.site.site_url = settings.SITE_URL
