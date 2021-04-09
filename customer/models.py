from django.db import models
from enderecos.models import Endereco
class Customer(models.Model):

    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=40, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name