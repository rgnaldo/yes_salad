from rest_framework.viewsets import ModelViewSet

from order.serializers import OrderSerializer
from order.models import Order


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
