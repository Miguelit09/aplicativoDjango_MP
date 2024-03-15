from django.db import models

# Create your models here.
class Persona(models.Model):
  nombre_persona = models.CharField(max_length=40, null=False, blank=False)
  edad_persona = models.IntegerField(null=False, blank=False)
  correo = models.EmailField(max_length=120, null=False, blank=False)
  telefono = models.CharField(max_length = 10, null=False, blank=False)
  numero_identidad = models.CharField(max_length=15, null=False, blank=False)

class Mascota(models.Model):
  OPCIONES_TIPO_MASCOTA = [
    ("Perro", "Opción 1"),
    ("Gato", "Opción 2"),
    ("Conejo", "Opción 3"),
    ("Tortuga", "Opción 4"),
    ("Paloma", "Opción 5")
  ]
  tipo_mascota = models.CharField(max_length=30, choices=OPCIONES_TIPO_MASCOTA, null=False, blank=False)
  nombre_mascota = models.CharField(max_length=40, null=False, blank=False)
  edad_mascota = models.IntegerField(null=True, blank=True)
  persona = models.OneToOneField(Persona, on_delete=models.CASCADE, null=False, blank=False)

