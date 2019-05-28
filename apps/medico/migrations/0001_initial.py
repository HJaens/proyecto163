# Generated by Django 2.2.1 on 2019-05-26 22:55

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfilmedico',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('tipo', models.CharField(default='Medico', max_length=20)),
                ('id_medico', models.IntegerField()),
                ('area', models.CharField(max_length=30)),
                ('especialidad', models.CharField(max_length=30)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='photosmedico')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]