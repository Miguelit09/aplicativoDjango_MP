# Generated by Django 5.0.2 on 2024-03-15 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_persona', models.CharField(max_length=40)),
                ('edad_persona', models.IntegerField()),
                ('correo', models.EmailField(max_length=120)),
                ('telefono', models.CharField(max_length=10)),
                ('numero_identidad', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_mascota', models.CharField(choices=[('Perro', 'Opción 1'), ('Gato', 'Opción 2'), ('Conejo', 'Opción 3'), ('Tortuga', 'Opción 4'), ('Paloma', 'Opción 5')], max_length=30)),
                ('nombre_mascota', models.CharField(max_length=40)),
                ('edad_mascota', models.IntegerField(blank=True, null=True)),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mascota.persona')),
            ],
        ),
    ]
