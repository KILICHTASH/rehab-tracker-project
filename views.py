from django.shortcuts import render
from .models import Patient

def index(request):
    patients = Patient.objects.all()
    return render(request, 'index.html', {'patients': patients})