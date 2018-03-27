from rest_framework.viewsets import ModelViewSet

from menu.serializers import MenuSerializer
from menu.models import Menu

class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer