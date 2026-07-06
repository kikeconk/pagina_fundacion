from django.shortcuts import render
from .models import Publicacion

def pagina_inicio(request, idioma_cod='es'):
    # Buscamos todas las publicaciones que coincidan con el código de idioma (es, en, fr, it)
    publicaciones = Publicacion.objects.filter(idioma=idioma_cod).order_by('fecha_creacion')
    
    # Lista de idiomas disponibles para pintar las pestañas en el diseño
    idiomas_disponibles = [
        {'codigo': 'es', 'nombre': 'Español'},
        {'codigo': 'en', 'nombre': 'English'},
        {'codigo': 'fr', 'nombre': 'Français'},
        {'codigo': 'it', 'nombre': 'Italiano'},
    ]
    
    contexto = {
        'publicaciones': publicaciones,
        'idioma_actual': idioma_cod,
        'idiomas': idiomas_disponibles,
    }
    return render(request, 'publicaciones/index.html', contexto)