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
    # função vai listar apenas as pessoas com cargo de id 1
 
    pessoas = Pessoa.objects.filter(cargo__pk = 2)  
    return render(request, 'listar.html', {'pessoas': pessoas})