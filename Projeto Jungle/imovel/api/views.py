from rest_framework.viewsets import ModelViewSet
from imovel.api.serializers import ImovelSerializer, ReservaSerializer
from imovel.models import Imovel, Reserva

class ImovelViewSet(ModelViewSet):
    serializer_class = ImovelSerializer
    queryset = Imovel.objects.all()

class ReservaViewSet(ModelViewSet):
    serializer_class = ReservaSerializer
    queryset = Reserva.objects.all()