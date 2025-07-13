import time

from django.urls import path
from django.contrib import admin
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from utils.meetings_parser import import_file, OnCollision
from apps.meetings.exceptions import InvalidDocumentStructure
from apps.meetings.data.models import ImportedFile


@admin.register(ImportedFile)
class ImportedFileAdmin(admin.ModelAdmin):
    add_form_template = 'admin/imported_file/add_form.html'
    readonly_fields = ['filename', 'errors']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('process-import/', self.process_import),
        ]
        return custom_urls + urls

    def process_import(self, request):
        files = request.FILES.getlist('files')
        on_collision = OnCollision(int(request.POST.get('action')))

        log_messages = []
        for file in files:
            try:
                message_generator = import_file(file, on_collision)
                log_messages.extend(list(message_generator))
            except InvalidDocumentStructure as e:
                log_messages.append(e)

        return JsonResponse(log_messages, safe=False)
