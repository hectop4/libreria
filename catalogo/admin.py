from django.contrib import admin
from .models import Libro, Editorial, Resena

# Register your models here.

admin.site.register(Libro)
admin.site.register(Editorial)
admin.site.register(Resena)