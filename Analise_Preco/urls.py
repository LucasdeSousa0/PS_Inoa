from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro-usuario/', views.cadastro_usuario, name='cadastro-usuario'),
    path('receber-ativo/', views.receber_ativos, name='receber-ativo'),
    path('acompanhar-ativo/', views.acompanhar_ativos, name='acompanhar-ativo'),
    path('Ativo_certo/', views.Ativo_certo, name='Ativo_certo'),
    path('remover-ativo', views.remover_ativo, name='remover-ativo'),
    path('confirmacao/', views.confirmacao_cadastro, name='confirmacao_cadastro'),
]