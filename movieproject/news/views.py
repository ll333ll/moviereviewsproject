from django.shortcuts import render
from .models import News

def news_view(request):
    news = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'news': news})
