from rest_framework import serializers
from imovel.models import Imovel, Reserva

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = ['id', 'titulo', 'descricao', 'endereco', 'preco', 'locador']

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'imovel', 'cliente', 'data_inicio', 'data_fim', 'status']
