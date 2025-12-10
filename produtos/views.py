from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Produto
from .forms import ProdutoForm

def cardapio(request):
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, "produtos/cardapio.html", {"produtos": produtos})

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos/produto_form.html"
    success_url = reverse_lazy("cardapio")

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos/produto_form.html" 
    success_url = reverse_lazy("cardapio")

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = "produtos/produto_confirm_delete.html" 
    success_url = reverse_lazy("cardapio")
    
def api_listar_produtos(request):
    produtos = Produto.objects.all()
    
    data = []
    for p in produtos:
        item = {
            "id": p.id,
            "nome": p.nome,
            "descricao": p.descricao,
            "preco": float(p.preco), 
            "categoria": p.categoria.nome, 
            "disponivel": p.disponivel
        }
        data.append(item)
    
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})