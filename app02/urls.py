from django.urls import path
from .views import lista_livros, detalhe_livro#, adicionar_livro

urlpatterns = [
    path('', lista_livros),
    path('<int:id>/', detalhe_livro, name='detalhe_livro'),
    #path('novo/', adicionar_livro),
]