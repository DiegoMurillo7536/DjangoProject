# Generated by Django 4.1.3 on 2022-11-04 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='number',
            field=models.SmallIntegerField(verbose_name='Número'),
        ),
    ]
