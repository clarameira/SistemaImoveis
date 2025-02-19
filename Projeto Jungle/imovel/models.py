from django.db import models
# Create your models here.

class Imovel(models.Model):
    titulo = models.CharField(max_length=140)
    descricao = models.CharField(max_length=320)
    endereco = models.CharField(max_length=140)
    preco = models.FloatField()

class Reserva(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, null = True)
    cliente = models.CharField(max_length=320)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    status = models.CharField(max_length=60)