from django.urls import path
from galeria.views import index, imagem, buscar


urlpatterns = [
    path('', index, name='index'), # Rota para a página inicial da galeria
    path('imagem/<int:foto_id>', imagem, name='imagem'), # Rota para visualizar uma imagem específica
    path('buscar/', buscar, name='buscar'),  # Rota para busca de fotografias
    #... outras rotas podem ser adicionadas aqui   
    
]