from django.db import models

class Computador(models.Model):
    equipamento = models.CharField(max_length=100)
    origem = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    manutencao = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    dataSaida = models.CharField(max_length=100)