from django.shortcuts import render
from usuarios.forms import LoginForms

def login(request):
    form = LoginForms() # Instancia o formulário de login
    return render(request, 'usuarios/login.html', {'form': form}) # Renderiza o template login.html e passa o formulário como contexto

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')