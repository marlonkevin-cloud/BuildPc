from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Perfil, Setup


class CadastroUsuarioForm(UserCreationForm):

    first_name = forms.CharField(
        label='Nome completo',
        max_length=150,
        required=True
    )

    email = forms.EmailField(
        label='E-mail',
        required=True
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password1',
            'password2'
        ]

        labels = {
            'username': 'Nome de usuário',
        }


class PerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ['telefone']

        labels = {
            'telefone': 'Telefone',
        }


class SetupForm(forms.ModelForm):

    class Meta:
        model = Setup
        fields = ['nome', 'pecas']

        labels = {
            'nome': 'Nome do plano de montagem',
            'pecas': 'Peças selecionadas',
        }

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: PC Gamer'
            }),

            'pecas': forms.CheckboxSelectMultiple(),
        }