from django.contrib import admin
from apps.meetings.data.models import Meeting, Question, Tag


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'protocol_number', 'meeting_type', 'deputies', 'presiding', 'quorum']
    inlines = [QuestionInline]

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "position_1870":
            kwargs["choices"] = [(value, f"{value} {label}") for value, label in db_field.choices]
        elif db_field.name == "position_1892":
            kwargs["choices"] = [(value, f"{value}. {label}") for value, label in db_field.choices]
        return super().formfield_for_choice_field(db_field, request, **kwargs)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

