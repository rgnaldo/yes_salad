from rest_framework.serializers import ModelSerializer

from order.serializers import OrderSerializer
from buy.serializers import BuySerializer
from .models import Order


class BuySerializer(ModelSerializer):
    order = OrderSerializer

    class Meta:
        model = Order
        fields = [
            '__all__', 'order',
            ]
