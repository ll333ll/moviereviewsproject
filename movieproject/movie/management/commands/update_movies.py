from django.core.management.base import BaseCommand
from movie.models import Movie
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Actualizar las películas para asegurarse de que tienen género, año e imagen por defecto'

    def handle(self, *args, **kwargs):
        default_image_path = "images/default.jpg"
        
        # Iterar sobre todas las películas en la base de datos
        for movie in Movie.objects.all():
            if not movie.genre:
                movie.genre = "Desconocido"  # Género por defecto

            if not movie.year:
                movie.year = 2000  # Año por defecto

            if not movie.image:
                movie.image = default_image_path  # Asignar imagen por defecto

            movie.save()

        self.stdout.write(self.style.SUCCESS('Películas actualizadas correctamente.'))
