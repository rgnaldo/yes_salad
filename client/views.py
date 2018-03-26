from rest_framework.viewsets import ModelViewSet

from client import serializers
from client.models import Client


class ClientViewSet(ModelViewSet):
    serializer_class = serializers.ClientSerializer
    queryset = Client.objects.all()
