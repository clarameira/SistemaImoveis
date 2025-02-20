from rest_framework.viewsets import ModelViewSet
from imovel.api.serializers import ImovelSerializer, ReservaSerializer
from imovel.models import Imovel, Reserva

class ImovelViewSet(ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

class ReservaViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer