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
    # Trazer do banco de dados todas as pessoas que tem o cargo admin
    cargo = Cargos.objects.get(id = 2)
    pessoa_admin = Pessoa.objects.filter(cargo = cargo)
    print(pessoa_admin)

    pessoa = Pessoa.objects.all()

    
    return render(request, 'listar.html', {'pessoas': pessoa})