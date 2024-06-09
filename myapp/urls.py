from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),
    path('adicionar/', views.adicionar_livro, name='adicionar_livro'),
    path('atualizar/<int:pk>/', views.atualizar_livro, name='atualizar_livro'),
    path('excluir/<int:pk>/', views.excluir_livro, name='excluir_livro'),
]
