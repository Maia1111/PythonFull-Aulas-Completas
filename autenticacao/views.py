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
         cargo = Cargos.objects.filter(id = 1).first()
         

         pessoa = Pessoa(nome=nome, email=email, senha=senha, cargo=cargo)
         pessoa.save()
         return HttpResponse('Cadatrado com sucesso')
    

   
def listar(request):
   if len(request.GET) != 0:
       nome = request.GET.get('nome')
       email = request.GET.get('email')
       senha = request.GET.get('senha')
       cargo = Cargos.objects.filter(id = 1).first()
       pessoa = Pessoa(nome=nome, email=email, senha=senha, cargo=cargo)
       pessoa.save()
       print(pessoa)

   pessoas = Pessoa.objects.all()
   return render(request, 'listar.html', {'pessoas': pessoas})


  