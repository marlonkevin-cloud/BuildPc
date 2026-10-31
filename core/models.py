from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Peca(models.Model):
    nome = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='pecas'
    )

    descricao = models.TextField(blank=True)

    def __str__(self):
        return f'{self.nome} - {self.marca}'


class Perfil(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil'
    )

    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.usuario.username


class Setup(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='setups'
    )

    nome = models.CharField(max_length=150)

    pecas = models.ManyToManyField(
        Peca,
        related_name='setups',
        blank=True
    )

    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - {self.usuario.username}'