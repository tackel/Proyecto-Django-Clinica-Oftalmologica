# Generated by Django 3.1.2 on 2020-11-18 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaApp', '0015_remove_pedido_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='precio',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]