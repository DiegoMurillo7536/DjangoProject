# Generated by Django 4.1.3 on 2022-11-04 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_team_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='shield',
            field=models.ImageField(blank=True, null=True, upload_to='static/img', verbose_name='Escudo'),
        ),
    ]
