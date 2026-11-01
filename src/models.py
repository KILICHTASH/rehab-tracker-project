# src/models.py
# Модель пациента для трекера реабилитации

class Patient:
    def __init__(self, name, age, diagnosis):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        
    def get_info(self):
        return f"Пациент: {self.name}, Возраст: {self.age}, Диагноз: {self.diagnosis}"
