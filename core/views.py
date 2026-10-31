from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, 'core/index.html')

def montagem(request):
    if request.method == 'POST' or (request.method == 'GET' and 'nome_setup' in request.GET):
        # Adiciona a mensagem de sucesso ao clicar em Salvar Setup
        messages.success(request, 'Setup salvo com sucesso!')
        return redirect('core:perfil')

    return render(request, 'core/montagem.html')

def login_view(request):
    if request.method == 'POST' or (request.method == 'GET' and 'email' in request.GET):
        # Adiciona a mensagem de sucesso ao criar conta / logar
        messages.success(request, 'Conta acessada / criada com sucesso!')
        return redirect('core:perfil')

    return render(request, 'core/login.html')

def perfil(request):
    return render(request, 'core/perfil.html', {'setups': []})