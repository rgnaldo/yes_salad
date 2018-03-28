from django.db import models
from django.db.models import ForeignKey, DateTimeField, PROTECT

from client.models import Client
from menu.models import Menu


class Order(models.Model):
    client = ForeignKey(Client, on_delete=PROTECT,)
    menu = ForeignKey(Menu, on_delete=PROTECT,)
    creation_date = DateTimeField(auto_now_add=True)
