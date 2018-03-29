from django.db.models import (
    Model,
    CharField,
)


class Client(Model):
    name = CharField('Nome', max_length=100)
    address = CharField('Endereço', max_length=100)
    contact = CharField('Contato', max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return "{0}".format(self.name)
