from rest_framework.viewsets import ModelViewSet

from buy.serializers import BuySerializer
from buy.models import Buy


class BuyViewSet(ModelViewSet):
    queryset = Buy.objects.all()
    serializer_class = BuySerializer