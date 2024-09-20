from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('salvar/', views.salvar, name='salvar'),
    path('apagar/<int:id>', views.apagar, name='apagar')
]
