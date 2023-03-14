from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def cadastro(requests):


  pessoa = [{'nome':'Caio', 'idade': 13, 'profissão': 'Programador'},
            {'nome':'Marcos', 'idade': 22, 'profissão': 'Analista de sistema'},
            {'nome':'Paulo', 'idade': 14, 'profissão': 'Jogador'},
            {'nome':'Fabricio', 'idade': 15, 'profissão': 'Policial'},
            {'nome':'Jose', 'idade': 40, 'profissão': 'Administrador'},
                          
            ]
  return render(requests, 'index.html', {'pessoa': pessoa})
