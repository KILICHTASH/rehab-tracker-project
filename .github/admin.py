from django.contrib import admin
from .models import Patient, HealthDiary, Medication

admin.site.register(Patient)
admin.site.register(HealthDiary)
admin.site.register(Medication)