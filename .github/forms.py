from django import forms
from .models import HealthDiary

class HealthDiaryForm(forms.ModelForm):
    class Meta:
        model = HealthDiary
        fields = ['date', 'feeling_score', 'notes'] # Поля, которые заполняет пациент