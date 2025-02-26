from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib, base64
from collections import Counter
from .models import Movie

def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

def about(request):
    return render(request, 'about.html')

def statistics_view(request):
    # Obtener datos de películas
    movies_by_year = Movie.objects.values_list('year', flat=True)
    year_counts = Counter(movies_by_year)

    movies_by_genre = Movie.objects.values_list('genre', flat=True)
    genre_counts = Counter(movies_by_genre)

    def generate_graph(data, title, xlabel, ylabel):
        plt.figure(figsize=(8, 4))
        plt.bar(data.keys(), data.values(), color='red')
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.title(title, fontsize=14)
        plt.xticks(rotation=45)

        buffer = io.BytesIO()
        plt.savefig(buffer, format="png", bbox_inches="tight")
        buffer.seek(0)
        return base64.b64encode(buffer.getvalue()).decode("utf-8")

    year_graph = generate_graph(year_counts, "Películas por Año", "Año", "Cantidad")
    genre_graph = generate_graph(genre_counts, "Películas por Género", "Género", "Cantidad")

    return render(request, 'statistics.html', {'year_graph': year_graph, 'genre_graph': genre_graph})

def signup(request):
    email = request.GET.get('email', 'No especificado')
    return render(request, 'signup.html', {'email': email})
