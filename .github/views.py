from django.shortcuts import render, redirect
from .models import Patient, HealthDiary, Medication
from .forms import HealthDiaryForm

# 1. Главная страница (её не хватает!)
def index(request):
    patients = Patient.objects.all()
    return render(request, 'index.html', {'patients': patients})

# 2. Дневник с формой
def diary_list(request):
    if request.method == 'POST':
        form = HealthDiaryForm(request.POST)
        if form.is_valid():
            diary_entry = form.save(commit=False)
            diary_entry.patient = Patient.objects.first()
            diary_entry.save()
            return redirect('diary')
    else:
        form = HealthDiaryForm()

    diaries = HealthDiary.objects.all()
    return render(request, 'diary.html', {'diaries': diaries, 'form': form})

# 3. Лекарства
def meds_list(request):
    meds = Medication.objects.all()
    return render(request, 'meds.html', {'meds': meds})


def doctor_dashboard(request):
    # Берем все записи дневника
    diaries = HealthDiary.objects.all().order_by('date')

    # Готовим данные для графика: список дат и список оценок
    dates = [d.date.strftime("%d.%m") for d in diaries]
    scores = [d.feeling_score for d in diaries]

    return render(request, 'doctor.html', {'dates': dates, 'scores': scores})