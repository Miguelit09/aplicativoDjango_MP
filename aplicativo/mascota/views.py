from django.http import HttpResponse
from django.shortcuts import render
from .models import Persona, Mascota

# Create your views here.
def index(request):
  personas = Persona.objects.all()
  return render(request, 'index.html', {
    'personas': personas
  })

def storage_persona(request, nombre_persona, edad_persona, correo, telefono, numero_identidad):
  persona = Persona(nombre_persona=nombre_persona, edad_persona=edad_persona, correo=correo, telefono=telefono, numero_identidad=numero_identidad)
  persona.save()
  return HttpResponse("Persona registrada")

def storage_mascota(request, tipo_mascota, nombre_mascota, edad_mascota, persona_id):
  mascota = Mascota(tipo_mascota=tipo_mascota, nombre_mascota=nombre_mascota, edad_mascota=edad_mascota, persona_id=persona_id)
  mascota.save()
  return HttpResponse("Mascota registrada")
