from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=40)
    preco = models.DecimalField(max_length=7, max_digits=2)
