from django.db import models

class Empresa(models.Model):
    empresa = models.CharField(max_length=99)
    cnpj = models.DecimalField(max_digits=14, decimal_places= 0)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return f"{self.empresa} {self.email}"