from django.db import models

class Patient(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    age = models.IntegerField(verbose_name="Возраст")
    diagnosis = models.CharField(max_length=200, verbose_name="Диагноз")

    def __str__(self):
        return self.full_name

class HealthDiary(models.Model):
    # Связываем запись с конкретным пациентом
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Пациент")
    date = models.DateField(verbose_name="Дата записи")
    feeling_score = models.IntegerField(verbose_name="Самочувствие (от 1 до 10)")
    notes = models.TextField(verbose_name="Комментарий", blank=True)

    def __str__(self):
        return f"{self.patient.full_name} - {self.date}"

class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Пациент")
    name = models.CharField(max_length=100, verbose_name="Название лекарства")
    time_to_take = models.TimeField(verbose_name="Время приема")
    is_active = models.BooleanField(default=True, verbose_name="Активно")

    def __str__(self):
        return f"{self.name} для {self.patient.full_name}"