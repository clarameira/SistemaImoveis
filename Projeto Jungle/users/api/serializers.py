from rest_framework import serializers
from users.models import Usuario,Locador,Cliente, Reserva, Imovel

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'senha']
        extra_kwargs = {'senha': {'write_only': True}}

    def create(self, validated_data):
        senha = validated_data.pop('senha', None)
        usuario = super().create(validated_data)
        if senha:
            usuario.set_password(senha)
            usuario.save()
        return usuario

class LocadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locador
        fields = ['id', 'nome', 'email', 'cnpj']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email', 'cpf']

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = ['id', 'nome', 'endereco']  # Ou os campos que você deseja exibir

class ReservaSerializer(serializers.ModelSerializer):
    imovel = ImovelSerializer()

    class Meta:
        model = Reserva
        fields = ['id', 'imovel', 'data_inicio', 'data_fim']