# Generated by Django 4.1.3 on 2022-11-04 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_gameposition_alter_team_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('datebirth', models.DateField(verbose_name='Nacimiento')),
                ('role', models.CharField(choices=[('Técnico', 'Tecnico'), ('Asistente', 'Asistente'), ('Médico', 'Medico'), ('Preparador', 'Preparador')], default='Técnico', max_length=20)),
                ('nation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.team', verbose_name='Nacionalidad')),
            ],
            options={
                'verbose_name': 'Técnico',
                'verbose_name_plural': 'Técnicos',
                'db_table': 'tecnicos',
                'ordering': ['id'],
            },
        ),
    ]
