from django.db.models import (
    Model,
    ForeignKey,
    DateTimeField,
    PROTECT,
    IntegerField,
    DecimalField,
)

from client.models import Client
from menu.models import Menu


class Order(Model):
    client = ForeignKey(Client, on_delete=PROTECT,)
    menu = ForeignKey(Menu, on_delete=PROTECT,)
    creation_date = DateTimeField(auto_now_add=True)
    quantity = IntegerField(verbose_name='Quantidade')
    total_value = DecimalField('Valor Total', max_digits=10, decimal_places=2)
