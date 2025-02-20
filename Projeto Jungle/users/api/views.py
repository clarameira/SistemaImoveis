from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import AllowAny
from users.api.serializers import UsuarioSerializer, LocadorSerializer, ClienteSerializer
from users.models import Usuario, Locador, Cliente
from rest_framework import status
from users.models import Imovel, Reserva 
from users.api.serializers import ImovelSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class LocadorViewSet(ModelViewSet):
    queryset = Locador.objects.all()
    serializer_class = LocadorSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class BuscaImovelViewSet(ViewSet):
    
    def list(self, request):
        
        filtros = request.query_params
        imoveis = Imovel.objects.filter(**filtros.dict())
        
        if not imoveis.exists():
            return Response({"mensagem": "Nenhum imóvel encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ImovelSerializer(imoveis, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
       
        try:
            imovel = Imovel.objects.get(pk=pk)
        except Imovel.DoesNotExist:
            return Response({"erro": "Imóvel não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ImovelSerializer(imovel)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def check_disponibilidade(self, request, pk=None):
       
        try:
            imovel = Imovel.objects.get(pk=pk)
        except Imovel.DoesNotExist:
            return Response({"erro": "Imóvel não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        data_inicio = request.query_params.get("data_inicio")
        data_fim = request.query_params.get("data_fim")
        
        if not data_inicio or not data_fim:
            return Response({"erro": "Datas de início e fim são obrigatórias."}, status=status.HTTP_400_BAD_REQUEST)
        
        reserva_existente = Reserva.objects.filter(imovel=imovel, data_inicio__lte=data_fim, data_fim__gte=data_inicio).exists()
        
        if reserva_existente:
            return Response({"disponivel": False, "mensagem": "Imóvel não disponível para o período selecionado."}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"disponivel": True, "mensagem": "Imóvel disponível."}, status=status.HTTP_200_OK)
    
    def reservar(self, request, pk=None):
    
        try:
            imovel = Imovel.objects.get(pk=pk)
        except Imovel.DoesNotExist:
            return Response({"erro": "Imóvel não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        data_inicio = request.data.get("data_inicio")
        data_fim = request.data.get("data_fim")
        
        if not data_inicio or not data_fim:
            return Response({"erro": "Datas de início e fim são obrigatórias."}, status=status.HTTP_400_BAD_REQUEST)
        
        reserva_existente = Reserva.objects.filter(imovel=imovel, data_inicio__lte=data_fim, data_fim__gte=data_inicio).exists()
        
        if reserva_existente:
            return Response({"erro": "Imóvel não disponível para o período selecionado."}, status=status.HTTP_400_BAD_REQUEST)
        
        reserva = Reserva.objects.create(imovel=imovel, data_inicio=data_inicio, data_fim=data_fim)
        return Response({"mensagem": "Reserva realizada com sucesso!", "reserva_id": reserva.id}, status=status.HTTP_201_CREATED)
