from django.contrib import admin
from .models import Alumno

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('run','nombres','apellido_paterno','apellido_materno')

admin.site.register(Alumno, AlumnoAdmin)
