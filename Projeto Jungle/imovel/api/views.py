from rest_framework.viewsets import ModelViewSet
from imovel.api.serializers import ImovelSerializer, ReservaSerializer
from imovel.models import Imovel, Reserva
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImovelSerializer, ReservaSerializer
from django.utils.dateparse import parse_date

class ImovelViewSet(ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

class ReservaViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class BuscaImovelViewSet(ViewSet):
    """
    ViewSet para busca de imóveis com filtros e verificação de disponibilidade para reserva.
    """
    
    def list(self, request):
        """
        Busca imóveis com base nos filtros fornecidos pelo cliente.
        """
        filtros = request.query_params
        imoveis = Imovel.objects.filter(**filtros.dict())
        
        if not imoveis.exists():
            return Response({"mensagem": "Nenhum imóvel encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ImovelSerializer(imoveis, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """
        Retorna os detalhes de um imóvel específico.
        """
        try:
            imovel = Imovel.objects.get(pk=pk)
        except Imovel.DoesNotExist:
            return Response({"erro": "Imóvel não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ImovelSerializer(imovel)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def check_disponibilidade(self, request, pk=None):
        """
        Verifica a disponibilidade de um imóvel para o período desejado.
        """
        imovel = Imovel.objects.get(pk=pk)
        data_inicio = request.query_params.get("data_inicio")
        data_fim = request.query_params.get("data_fim")
        
        if not data_inicio or not data_fim:
            return Response({"erro": "Datas de início e fim são obrigatórias."}, status=status.HTTP_400_BAD_REQUEST)
        
        reserva_existente = Reserva.objects.filter(imovel=imovel, data_inicio__lte=data_fim, data_fim__gte=data_inicio).exists()
        
        if reserva_existente:
            return Response({"disponivel": False, "mensagem": "Imóvel não disponível para o período selecionado."}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"disponivel": True, "mensagem": "Imóvel disponível."}, status=status.HTTP_200_OK)
    
    def reservar(self, request, pk=None):
        """
        Cria uma reserva para um imóvel disponível.
        """
        imovel = Imovel.objects.get(pk=pk)
        data_inicio = request.data.get("data_inicio")
        data_fim = request.data.get("data_fim")
        
        if not data_inicio or not data_fim:
            return Response({"erro": "Datas de início e fim são obrigatórias."}, status=status.HTTP_400_BAD_REQUEST)
        
        reserva_existente = Reserva.objects.filter(imovel=imovel, data_inicio__lte=data_fim, data_fim__gte=data_inicio).exists()
        
        if reserva_existente:
            return Response({"erro": "Imóvel não disponível para o período selecionado."}, status=status.HTTP_400_BAD_REQUEST)
        
        reserva = Reserva.objects.create(imovel=imovel, data_inicio=data_inicio, data_fim=data_fim)
        return Response({"mensagem": "Reserva realizada com sucesso!", "reserva_id": reserva.id}, status=status.HTTP_201_CREATED)
