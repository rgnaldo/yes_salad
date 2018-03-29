from rest_framework.serializers import ModelSerializer

from client.serializers import ClientSerializer
from menu.serializers import MenuSerializer
from .models import Order


class OrderSerializer(ModelSerializer):
    client = ClientSerializer
    menu = MenuSerializer

    class Meta:
        model = Order
        fields = [
            'client', 'menu',  'creation_date', 'quantity', 'total_value',
            ]
