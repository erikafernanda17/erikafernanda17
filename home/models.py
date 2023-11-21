from django.db import models


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=200)
    sobrenome = models.TextField(max_length=200)
    email = models.EmailField(max_length=200)
