from django.contrib import admin

from apps.meetings.data.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['title']
