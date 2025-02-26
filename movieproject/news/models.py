from django.db import models

class News(models.Model):
    headline = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news/', null=True, blank=True)

    def __str__(self):
        return self.headline
