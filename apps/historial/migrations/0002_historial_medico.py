# Generated by Django 2.2.1 on 2019-05-26 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('historial', '0001_initial'),
        ('medico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historial',
            name='medico',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='medico.Perfilmedico'),
        ),
    ]
