from django.db import models


class Client(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100)
    address = models.CharField(verbose_name='Endereço', max_length=100)
    contact = models.CharField(verbose_name='Contato', max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return "{0}".format(self.name)
