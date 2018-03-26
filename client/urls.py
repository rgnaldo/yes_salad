
from django.urls import path
from client.views import ClientViewSet


urlpatterns = [
    path('client', ClientViewSet)
]
