from django.db import models

from .people import People

class Equipe(models.Model):
    equipe = models.CharField(max_length=99)
    integrantes = models.ManyToManyField(People, verbose_name=("participantes"))
    qtdi = models.DecimalField(max_digits=14, decimal_places= 0)
    
    def __str__(self):
        return f"{self.equipe} {self.integrantes} ({self.qtdi})"