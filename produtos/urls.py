from django.urls import path
from . import views

urlpatterns = [
    path("", views.cardapio, name="cardapio"),
    path("novo/", views.ProdutoCreateView.as_view(), name="produto_novo"),
    path("editar/<int:pk>/", views.ProdutoUpdateView.as_view(), name="produto_editar"),
    path("excluir/<int:pk>/", views.ProdutoDeleteView.as_view(), name="produto_excluir"),
    path("api/produtos/", views.api_listar_produtos, name="api_produtos"),
]