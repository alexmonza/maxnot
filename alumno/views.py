from django.views.generic import ListView, DetailView, CreateView
from .models import Alumno

class AlumnoList(ListView):
    queryset = Alumno.objects.all()

class AlumnoDetail(DetailView):
    model = Alumno



class AlumnoCreate(CreateView):
    model = Alumno
    fields = ['run','nombres','apellido_paterno','apellido_materno','genero','fecha_nacimiento','religion']





