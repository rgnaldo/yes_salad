from django.db.models import(
    DecimalField,
    IntegerField,
    Model,
)

from django.db.models import ForeignKey, DateTimeField, PROTECT

from order.models import Order

class Buy(Model):
    order = ForeignKey(Order, on_delete=PROTECT, )
    creation_date = DateTimeField(auto_now_add=True)
    total_value = DecimalField('Valor Total', max_digits=10, decimal_places=2)