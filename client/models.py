from django.db import models


class Client(models.Model):
    name = models.CharField(verbose_name='name', max_length=100)
    address = models.CharField(verbose_name='address', max_length=100)
    contact = models.CharField(verbose_name='contact', max_length=20)

    def __str__(self):
        return "{0}".format(self.name)
