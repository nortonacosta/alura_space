from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('admin/', admin.site.urls), # Rota para o admin
        path('', include('galeria.urls')), # Rota para o app galeria
        path('', include('usuarios.urls')),  # Rota para o app usuarios
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
