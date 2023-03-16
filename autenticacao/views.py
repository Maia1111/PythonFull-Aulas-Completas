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
    # Alterando um campo 
    cargo = Cargos.objects.get(id = 1)
    pessoa = Pessoa.objects.get(id = 3) 
   
    pessoa.cargo = cargo
    pessoa.save()

    
    return render(request, 'listar.html', {'pessoas': pessoa})