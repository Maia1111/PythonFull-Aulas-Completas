from django.template import Library


register = Library()


@register.filter(name='teste')
def teste(v1):
    if v1 == 3:
     return f"Seu id: {v1} portando vc é um cliente master"
    else:
       return v1