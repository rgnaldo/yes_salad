from rest_framework.viewsets import ModelViewSet

from client.serializers import ClientSerializer
from client.models import Client


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
