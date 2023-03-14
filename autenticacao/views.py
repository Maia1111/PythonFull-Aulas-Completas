from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def cadastro(requests): 
   nome = requests.GET.get('nome')
   sobrenome = requests.GET.get('sobrenome')
   idade = requests.GET.get('idade')
   print(nome, sobrenome, idade) 
   return render(requests, 'index.html', {'nome': nome, 'sobrenome': sobrenome, 'idade': idade})

