from django.shortcuts import redirect, render
from django.http import HttpResponse

#importação de models
from .models import Pessoa

# Create your views here.
def home(request) -> HttpResponse:
    pessoas = Pessoa.objects.all()
    return render(request, 'index.html', {"pessoas": pessoas})

def salvar(request) -> HttpResponse:
    nome = request.POST.get("nome")
    Pessoa.objects.create(nome=nome)
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id) #procura 
    return render(request, "edit.html", {"pessoa":pessoa})

def update(request, id):
    novo_nome = request.POST.get("novo_nome")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = novo_nome
    pessoa.save()
    return redirect(home)