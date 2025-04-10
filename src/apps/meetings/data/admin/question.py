from django.contrib import admin

from apps.meetings.data.models import Question
from apps.meetings.data.forms import QuestionAdminForm


class QuestionInline(admin.StackedInline):
    form = QuestionAdminForm
    model = Question
    fieldsets = (
        (None, {
            'fields': (
                'number',
                'description',
                'quorum',
                'position_1870',
                'position_1892',
                'author_classification',
                'solution',
                'solution_content',
                'tags',
                'case_number',
                'sheet_start',
                'sheet_end',
            )
        }),
    )
    autocomplete_fields = ['tags']
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


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    fieldsets = (
        (None, {
            'fields': (
                'number',
                'description',
                'quorum',
                'position_1870',
                'position_1892',
                'author_classification',
                'solution',
                'solution_content',
                'tags',
                'case_number',
                'sheet_start',
                'sheet_end',
            )
        }),
    )
    autocomplete_fields = ['tags']
