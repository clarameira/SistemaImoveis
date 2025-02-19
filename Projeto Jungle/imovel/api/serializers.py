from rest_framework import serializers
from imovel.models import Imovel, Reserva

class ImovelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Imovel
        fields = ['id', 'titulo', 'descricao', 'endereco', 'preco']

class ReservaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserva
        fields = "__all__"