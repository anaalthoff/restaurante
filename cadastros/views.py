from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request, 'index.html', {'nome' : 'Bom Gosto'})

def historia(request):
    return render(request, 'historia.html', {'nome' : 'Bom Gosto'})

def cardapio(request):
    return render(request, 'cardapio.html', {'nome' : 'Bom Gosto'})