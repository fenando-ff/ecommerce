from django.db import models

# Create your models here.
class PRODUTO(models.Model):
    nome = models.CharField(max_length=80, unique=True)
    descricao = models.TextField(max_length=200)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome
    