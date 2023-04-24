from django.contrib import admin
from .models import Projektas, Klientas, Darbuotojas, Darbas, Saskaita

admin.site.register(Projektas)
admin.site.register(Klientas)
admin.site.register(Darbuotojas)
admin.site.register(Darbas)
admin.site.register(Saskaita)