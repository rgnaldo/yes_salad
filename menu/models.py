from django.db import models

class Menu(models.Model):
    descricao = models.CharField(verbose_name='Descricao', max_length=100)
    preco = models.FloatField(verbose_name='Preço', max_length=100)
    data = models.DateField(verbose_name='Data', max_length=20)

    class Meta:
        ordering = ['descricao']

    def __str__(self):
        return "{0}".format(self.descricao)