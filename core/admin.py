from django.contrib import admin
from .models import Categoria, Peca, Perfil, Setup


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)


@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'marca', 'preco', 'categoria')
    list_filter = ('categoria', 'marca')
    search_fields = ('nome', 'marca')


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'telefone')
    search_fields = ('usuario__username', 'telefone')


@admin.register(Setup)
class SetupAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'usuario', 'data_criacao')
    list_filter = ('data_criacao',)
    search_fields = ('nome', 'usuario__username')
    filter_horizontal = ('pecas',)