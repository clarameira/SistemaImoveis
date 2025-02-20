from django.db import models
# Create your models here.
from users.models import Locador,Cliente

class Imovel(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    endereco = models.CharField(max_length=255)
    preco = models.FloatField()
    locador = models.ForeignKey(Locador, on_delete=models.CASCADE, related_name='imoveis', null=True, blank=True)

    def get_detalhes(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'endereco': self.endereco,
            'preco': self.preco
        }

    def __str__(self):
        return self.titulo

# Modelo Reserva
class Reserva(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='reservas', null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas', null=True, blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    status = models.CharField(max_length=50, choices=[
        ('pendente', 'Pendente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada')
    ])

    def atualizar_status(self, status):
        self.status = status
        self.save()

    def __str__(self):
        return f"Reserva {self.id} - {self.status}"