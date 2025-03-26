from django.db import models
from django.contrib import admin
from django.forms import Select
from django_flatpickr.settings import FlatpickrOptions
from django_flatpickr.widgets import DatePickerInput
from apps.meetings.data.models import Meeting, Question, Tag


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "position_1870":
            kwargs["choices"] = [(value, f"{value} {label}") for value, label in db_field.choices]
        elif db_field.name == "position_1892":
            kwargs["choices"] = [(value, f"{value}. {label}") for value, label in db_field.choices]
        return super().formfield_for_choice_field(db_field, request, **kwargs)

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'protocol_number', 'meeting_type', 'deputies', 'presiding']
    inlines = [QuestionInline]

    formfield_overrides = {
        models.DateField: {'widget': DatePickerInput(
            options=FlatpickrOptions(
                altFormat='d F Y',
                allowInput=True,
                locale='ru',
            )
        )},
    }


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

