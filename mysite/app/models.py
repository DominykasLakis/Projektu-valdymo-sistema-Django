from django.db import models
from django.contrib.auth.models import User


class Projektas(models.Model):
    title = models.CharField('Pavadinimas', max_length=200, help_text='Įveskite projekto pavadinimą')
    start_date = models.DateField("Projekto pradžios data", help_text='Įveskite projekto pradžios datą')
    end_date = models.DateField("Projeko pabaigos data", help_text='Įveskite projekto pabaigos datą')
    client = models.ForeignKey("Klientas", on_delete=models.SET_NULL, null=True)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    workers = models.ForeignKey("Darbuotojas", on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey("Darbas", on_delete=models.SET_NULL, null=True)
    accounts = models.ForeignKey("Saskaita", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title} {self.start_date} {self.end_date}"

    class Meta:
        verbose_name_plural = "Projektai"


class Klientas(models.Model):
    first_name = models.CharField("Vardas", max_length=100)
    last_name = models.CharField("Pavardė", max_length=100)
    company = models.CharField("Įmonė", max_length=100)
    contacts = models.TextField("Kontaktai", max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.company}"

    class Meta:
        verbose_name_plural = "Klientai"


class Darbuotojas(models.Model):
    first_name = models.CharField("Vardas", max_length=100)
    last_name = models.CharField("Pavardė", max_length=100)
    position = models.CharField("Pareigos", max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.position}"

    class Meta:
        verbose_name_plural = "Darbuotojai"


class Darbas(models.Model):
    title = models.CharField("Pavadinimas", max_length=100)
    notes = models.TextField("Pastabos", max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Darbai"


class Saskaita(models.Model):
    date = models.DateField("Išrašymo data", auto_now_add=True)
    sum = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date} {self.sum}"

    class Meta:
        verbose_name_plural = "Sąskaitos"