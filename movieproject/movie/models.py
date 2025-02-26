from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    year = models.IntegerField(default=2000)
    genre = models.CharField(max_length=100, default="Desconocido")
    image = models.ImageField(upload_to='movies/', null=True, blank=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title