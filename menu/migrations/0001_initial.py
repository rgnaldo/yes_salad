# Generated by Django 2.0.3 on 2018-03-27 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descricao')),
                ('preco', models.FloatField(max_length=100, verbose_name='Preço')),
                ('data', models.DateField(max_length=20, verbose_name='Data')),
            ],
            options={
                'ordering': ['descricao'],
            },
        ),
    ]
