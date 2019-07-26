# Generated by Django 2.2 on 2019-07-26 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_auto_20190722_2132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quarto',
            options={'ordering': ('numero',), 'verbose_name': 'quarto', 'verbose_name_plural': 'quartos'},
        ),
        migrations.AlterModelOptions(
            name='reserva',
            options={'ordering': ('nome_cliente',), 'verbose_name': 'reserva', 'verbose_name_plural': 'reservas'},
        ),
        migrations.AddField(
            model_name='quarto',
            name='titulo',
            field=models.CharField(default='Quarto', max_length=200, verbose_name='título'),
            preserve_default=False,
        ),
    ]
