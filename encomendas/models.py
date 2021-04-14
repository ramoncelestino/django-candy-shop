from django.db import models
from customer.models import Customer

class Encomenda(models.Model):
    cliente = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, null=True)
    data_encomenda = models.DateTimeField()
    data_entrega = models.DateTimeField()

