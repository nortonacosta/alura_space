from django import forms

class LoginForms(forms.Form): 
    username = forms.CharField( # Nome de usuário, CharField é um campo de texto simples
        label='Nome de Usuário', 
        required=True, 
        max_length=100,
        widget=forms.TextInput( # Widget define o tipo de campo, TextInput é um campo de texto simples
            attrs={ # Atributos HTML adicionais para o campo
                   'class': 'form-control', # Classe CSS para estilização
                   'placeholder': 'Ex: joaodasilva' # Placeholder para o campo
            }
        )
    )        
    
    senha = forms.CharField( # Senha, widget define o tipo de campo, PasswordInput oculta os caracteres
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput( # Widget para campo de senha
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )        
    ) 