# Generated by Django 3.2.6 on 2021-08-08 22:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de criação'),
        ),
    ]
