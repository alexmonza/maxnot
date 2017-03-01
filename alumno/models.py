from django.db import models
from religion.models import Religion

class Alumno(models.Model):

    GENERO_CHOICES = (
        ('F','FEMENINO'),
        ('M','MASCULINO'),
    )


    run = models.CharField(max_length=9)
    nombres = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    genero = models.CharField(max_length=1,
                              choices=GENERO_CHOICES,)
    fecha_nacimiento = models.DateField()
    religion = models.ForeignKey(Religion)






