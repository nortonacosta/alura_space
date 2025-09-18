from django.shortcuts import render, get_object_or_404

from galeria.models import Fotografia



def index(request): # View para a página inicial da galeria        
    fotografias =  Fotografia.objects.order_by('data_foto').filter(publicada=True) # Filtra apenas as fotos publicadas (-"data_fotografia" para ordem decrescente)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id): # View para visualizar uma imagem específica
    fotografia = get_object_or_404(Fotografia, pk=foto_id) # Tenta obter a fotografia pelo ID, se não encontrar retorna 404
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request): # View para buscar fotografias
    fotografias =  Fotografia.objects.order_by('data_foto').filter(publicada=True)
    
    if 'buscar' in request.GET:
        nome_busca = request.GET['buscar']
        if nome_busca:
            fotografias = fotografias.filter(nome__icontains=nome_busca) # Filtra fotografias cujo nome contém o termo de busca, case insensitive    
    return render(request, 'galeria/buscar.html', {"cards": fotografias})    