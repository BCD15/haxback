from django.db import models

from .empresa import Empresa

class Avaliador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.DecimalField(max_digits=3, decimal_places= 0)
    email = models.EmailField(max_length=254)
    cpf = models.DecimalField(max_digits=11, decimal_places= 0)
    empresa = models.ForeignKey(Empresa, verbose_name=("empresa"), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.idade}) {self.email} {self.empresa}"
    
    class Meta:
        verbose_name_plural = "Avaliadores"