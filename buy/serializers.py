from rest_framework.serializers import ModelSerializer

from order.serializers import OrderSerializer
from .models import Buy


class BuySerializer(ModelSerializer):
    order = OrderSerializer

    class Meta:
        model = Buy
        fields = [
            'order',
            ]
