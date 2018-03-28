from rest_framework.routers import DefaultRouter

from order.views import OrderViewSet

urlpatterns = []

router = DefaultRouter()
router.register('', OrderViewSet)

urlpatterns = urlpatterns + router.urls
