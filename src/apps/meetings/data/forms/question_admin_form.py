from django import forms
from django.contrib import admin
from apps.meetings.data.models import Question


class QuestionAdminForm(forms.ModelForm):
    sheet_start = forms.DecimalField(max_digits=5, decimal_places=1, label='Начальный лист', required=True)
    sheet_end = forms.DecimalField(max_digits=5, decimal_places=1, label='Конечный лист', required=True)
    
    class Meta:
        model = Question
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.sheet_numbers:
            self.fields['sheet_start'].initial = self.instance.sheet_numbers[0] if len(self.instance.sheet_numbers) > 0 else None
            self.fields['sheet_end'].initial = self.instance.sheet_numbers[1] if len(self.instance.sheet_numbers) > 1 else None

    def clean(self):
        cleaned_data = super().clean()
        sheet_start = cleaned_data.get('sheet_start')
        sheet_end = cleaned_data.get('sheet_end')
        
        cleaned_data['sheet_numbers'] = [sheet_start, sheet_end]
        
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.sheet_numbers = self.cleaned_data['sheet_numbers']
        if commit:
            instance.save()
            self.save_m2m()
        return instance
