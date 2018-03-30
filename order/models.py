from django.db.models import (
    Model,
    ForeignKey,
    DateTimeField,
    PROTECT,
    IntegerField,

)

from client.models import Client
from menu.models import Menu


class Order(Model):
    client = ForeignKey(Client, verbose_name='Cliente', on_delete=PROTECT,)
    menu = ForeignKey(Menu, verbose_name='Cardápio', on_delete=PROTECT,)
    creation_date = DateTimeField(auto_now_add=True)
    quantity = IntegerField('Quantidade')

