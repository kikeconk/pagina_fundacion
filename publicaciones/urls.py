from django.urls import path
from . import views

urlpatterns = [
    # Raíz de la app (carga español por defecto)
    path('', views.pagina_inicio, name='inicio_defecto'),
    # Rutas dinámicas para los idiomas (/en/, /fr/, /it/)
    path('<str:idioma_cod>/', views.pagina_inicio, name='inicio_idioma'),
]