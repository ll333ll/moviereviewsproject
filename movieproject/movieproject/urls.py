from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from movie import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('about/', views.about, name='about'), 
    path('news/', include('news.urls')),
    path('statistics/', views.statistics_view, name='statistics'), 
    path('signup/', views.signup, name='signup'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
