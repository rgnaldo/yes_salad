from rest_framework.routers import DefaultRouter

from menu.views import MenuViewSet

urlpatterns = []

router = DefaultRouter()
router.register('', MenuViewSet)

urlpatterns = urlpatterns + router.urls
