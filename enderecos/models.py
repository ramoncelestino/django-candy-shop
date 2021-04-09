from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome

class Bairro(models.Model):
    nome = models.CharField(max_length=40)
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome

class Endereco(models.Model):

    rua = models.CharField(max_length=50)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=40, null=True, blank=True)
    bairro = models.ForeignKey(Bairro, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return "Bairro: " + self.bairro.nome + ", Rua: " + self.rua + ", Número: " + str(self.numero)