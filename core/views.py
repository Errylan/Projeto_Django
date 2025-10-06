from django.shortcuts import render
from .models import Area
from .forms import AreaForm

def index(request):
    return render (request, 'index.html')

def categorias(request):
    return render (request, 'categorias.html')

def  areas(request):
    areas = Area.objects.all()
    contexto ={
        'lista_areas': areas
    }
    return render (request, 'areas.html', contexto)

def area_cadastro(request):
    form = AreaForm(request.POST or None)
    contexto ={
        'form' :form
    }
    return render(request, 'area_cadastro.html', contexto)

