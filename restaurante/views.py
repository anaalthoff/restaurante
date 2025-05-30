from django.shortcuts import render

def index (request):
    return render(request, 'index.html', {'nome' : 'Bom Gosto'})

def historia(request):
    return render(request, 'historia.html', {'nome' : 'Bom Gosto'})