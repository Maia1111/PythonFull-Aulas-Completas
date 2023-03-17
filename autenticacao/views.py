from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from.models import *

def cadastro(request): 
    if request.method =="GET":
        return render(request, 'cadastro.html')
    
    elif request.method == "POST":
        
         nome = request.POST.get('nome')
         email = request.POST.get('email')
         senha = request.POST.get('senha')
         cargo = Cargos.objects.get(id=1)
         

         pessoa = Pessoa(nome=nome, email=email, senha=senha, cargo=cargo)
         pessoa.save()
         return HttpResponse('Cadatrado com sucesso')
    

   
def listar(request):
    # Trazer  todos os cargos de uma determinada pessoa

    pessoa  = Pessoa.objects.get(id = 3)
    cargos = Cargos.objects.filter(pessoa = pessoa )
    print(cargos)

    pessoas = Pessoa.objects.all()


    
    return render(request, 'listar.html', {'pessoas': pessoas})