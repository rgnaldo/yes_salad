from rest_framework.routers import DefaultRouter

from client.views import ClientViewSet

urlpatterns = []

router = DefaultRouter()
router.register('', ClientViewSet)

urlpatterns = urlpatterns + router.urls
