# Generated by Django 3.1.2 on 2020-11-20 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaApp', '0029_remove_turno_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]