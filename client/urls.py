from rest_framework.routers import DefaultRouter

from client.views import ClientViewSet


router = DefaultRouter()

router.register('', ClientViewSet)
