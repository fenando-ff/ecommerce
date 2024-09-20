from django.shortcuts import render, redirect
from .models import PRODUTO

# Create your views here.

def listar_produtos(request):
    produtos = PRODUTO.objects.all()
    return render(request, 'index.html', {'produtos': produtos})


def cadastro(request):
    return render(request, 'cadastro.html')

def salvar(request):
    nome = request.POST.get('nome')
    desc = request.POST.get('descricao')
    preco = request.POST.get('preco')
    categ = request.POST.get('categoria')
    PRODUTO.objects.create(nome = nome, descricao= desc, preco= preco, categoria=categ)
    return redirect(listar_produtos)

def apagar(request,id):
        produto = PRODUTO.objects.get(id=id)
        produto.delete()
        return redirect(listar_produtos)
        
