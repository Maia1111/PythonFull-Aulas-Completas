from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.http import HttpResponse

class Cargos(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    

class Pessoa(models.Model):
    foto = models.ImageField(upload_to='foto')
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    cargo = models.ManyToManyField(Cargos)

    def __str__(self):
        return self.nome
    
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"
    
    
    
    def get_foto(self):
        return mark_safe(f'<img style="width: 30px;" src="{self.foto.url}">')
    
class Pedido(models.Model):   
    nome = models.CharField(max_length=100)    
    quantidade = models.IntegerField()
    descricacao = models.TextField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.DO_NOTHING)



def mostra_pessoa(self):
    return HttpResponse('teste')


mostra_pessoa.label = "mostra pessoa"


