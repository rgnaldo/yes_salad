from django.db.models import (
    Model,
    DecimalField,
    DateField,
    CharField,
)


class Menu(Model):

    descricao = CharField('Descricao', max_length=100)
    price = DecimalField('Valor Unitario', max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['descricao']

    def __str__(self):
        return "{0}".format(self.descricao)