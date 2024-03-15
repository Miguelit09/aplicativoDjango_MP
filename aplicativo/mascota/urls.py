from . import views
from django.urls import path
# Create your tests here.

urlpatterns = [
  path("", views.index, name="lista_personas"),
  path("storage_persona/<str:nombre_persona>/<int:edad_persona>/<str:correo>/<str:telefono>/<str:numero_identidad>", views.storage_persona, name="storage_persona"),
  path("storage_mascota/<str:tipo_mascota>/<str:nombre_mascota>/<int:edad_mascota>/<int:persona_id>", views.storage_mascota, name="storage_mascota"),
]