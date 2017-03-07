from django.db import models

class Religion(models.Model):
    nombre_religion = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Religiones"

    def __str__(self):
        return '%s'%(self.nombre_religion)


