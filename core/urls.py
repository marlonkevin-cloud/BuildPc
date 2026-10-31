from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='index'),
    path('montagem/', views.montagem, name='montagem'),
    path('login/', views.login_view, name='login'),
    path('perfil/', views.perfil, name='perfil'),
]