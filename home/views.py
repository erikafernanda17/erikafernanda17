from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    return render(request, "home.html")

def cardapio(request):
    return render(request, "cardapio.html")

def cadastro(request):
    return render(request, "cadastro.html")

def usuarios(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.sobrenome = request.POST.get('sobrenome')
        novo_usuario.email = request.POST.get('email')
        novo_usuario.save()
        return redirect('usuarios')


    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, "usuarios.html", usuarios)
