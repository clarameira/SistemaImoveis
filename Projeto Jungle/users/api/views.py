from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from users.api.serializers import UsuarioSerializer, LocadorSerializer, ClienteSerializer
from users.models import Usuario,Locador,Cliente

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class LocadorViewSet(ModelViewSet):
    queryset = Locador.objects.all()
    serializer_class = LocadorSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer