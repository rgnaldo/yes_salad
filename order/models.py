from django.db.models import (
    Model,
    ForeignKey,
    DateTimeField,
    PROTECT,
    IntegerField,
    CharField,

)

from client.models import Client
from menu.models import Menu


class Order(Model):
    client = ForeignKey(Client, verbose_name='Cliente', on_delete=PROTECT,)
    menu = ForeignKey(Menu, verbose_name='Cardápio', on_delete=PROTECT,)
    creation_date = DateTimeField(auto_now_add=True)
    quantity = IntegerField('Quantidade')
    name = CharField('Nome', max_length=100)
    note = CharField('Observação', max_length=100)

