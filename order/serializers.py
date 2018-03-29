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
<<<<<<< 0ddf37c4a44782b2c24e2664bd4d6ef636212e4b
            'client', 'menu',  'creation_date', 'quantity', 'total_value',
=======
            'client', 'menu',
>>>>>>> erro serializers
            ]
