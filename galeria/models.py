from django.db import models
from datetime import datetime

class Fotografia(models.Model):
    
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("GALAXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
        ("ESTRELA", "Estrela")
    ]
    
    nome = models.CharField(max_length=100, null=False, blank=False) # Nome da fotografia
    legenda = models.CharField(max_length=150, null=False, blank=False) # Legenda curta para a foto
    categoria = models.CharField(max_length=100,choices=OPCOES_CATEGORIA, default='') # Categoria da foto, choices define as opções possíveis
    descricao = models.TextField(null=False, blank=False) # Descrição detalhada da foto
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True) # upload_to define o caminho onde a imagem será salva
    publicada = models.BooleanField(default=False) # Indica se a foto está publicada ou não, fazer filtro na view 
    data_foto = models.DateTimeField(default=datetime.now,  null=False, blank=False) # Data e hora da foto, default define o valor padrão

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"
