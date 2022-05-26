# Generated by Django 3.1.2 on 2020-11-20 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaApp', '0025_historial_medico_historial_medico'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medico',
            options={'verbose_name': 'medico', 'verbose_name_plural': 'medicos'},
        ),
        migrations.AddField(
            model_name='paciente',
            name='doctor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='medico', to='clinicaApp.medico'),
        ),
    ]