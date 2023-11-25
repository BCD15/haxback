from django.db import models

class People(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.DecimalField(max_digits=3, decimal_places= 0)
    email = models.EmailField(max_length=254)
    cpf = models.DecimalField(max_digits=11, decimal_places= 0)
    
    def __str__(self):
        return f"{self.nome} ({self.idade}) {self.email}"