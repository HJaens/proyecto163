# Generated by Django 2.2.1 on 2019-05-26 22:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nrohistoria', models.IntegerField()),
                ('hora', models.DateField(default=datetime.date.today)),
                ('caracteristica', models.TextField()),
                ('diagnostico', models.CharField(max_length=30)),
                ('receta', models.CharField(max_length=200)),
            ],
        ),
    ]
