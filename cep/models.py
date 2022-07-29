from django.db import models


class Cep(models.Model):
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=250)
    estado = models.CharField(max_length=250)
    bairro = models.CharField(max_length=250)
    rua = models.CharField(max_length=250)
    complemento = models.CharField(max_length=250, null=True)
