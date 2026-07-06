from django.db import models
from django.utils import timezone

class Publicacion(models.Model):
    OPCIONES_IDIOMA = [
        ('es', 'Español'),
        ('en', 'Inglés'),
        ('fr', 'Francés'),
        ('it', 'Italiano'),
    ]
    
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    idioma = models.CharField(max_length=2, choices=OPCIONES_IDIOMA, default='es')
    url_video = models.URLField(blank=True, null=True, help_text="Enlace del audiolibro o video de YouTube")
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"[{self.get_idioma_display()}] {self.titulo}"