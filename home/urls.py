from django.contrib import admin
from django.urls import path
from .views import home, cardapio, cadastro, usuarios

urlpatterns = [
    path('cardapio/', cardapio, name='cardapio'),
    path('cadastro/', cadastro, name="cadastro"),
    path('usuarios/', usuarios, name="usuarios"),
    path('', home, name='home'),
]