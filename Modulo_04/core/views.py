from django.shortcuts import render

from django.http import HttpResponse

# Uma 'view' é uma função que recebe um 'request' e retorna uma 'response'
def home(request):

    # Vamos retornar a resposta HTTP mais simples: um texto HTML
    return HttpResponse("<h1 style='color: green;'>Olá, Mundo! Esta é minha primeira página Django!</h1>")

def segundo(request):

    return HttpResponse("<h3 style='color: orange;'>Olá, Mundo! Esta é minha segunda página Django!</h3>")
