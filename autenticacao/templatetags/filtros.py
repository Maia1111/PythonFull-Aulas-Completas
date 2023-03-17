from django.template import Library


register = Library()


@register.filter(name='teste')
def teste(v1):
    return f"Seu valor: {v1}"