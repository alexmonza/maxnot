from django.db import models
from religion.models import Religion
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('alumno-detail', kwargs={'pk': self.pk})






