from django.db import models

class Patient(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    age = models.IntegerField(verbose_name="Возраст")
    diagnosis = models.CharField(max_length=200, verbose_name="Диагноз")

    def __str__(self):
        return self.full_name