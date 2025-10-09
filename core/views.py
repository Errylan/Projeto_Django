from django.shortcuts import render, redirect
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
    if form.is_valid():
        form.save()
        return redirect('areas')



    contexto ={
        'form' :form
    }
    return render(request, 'area_cadastro.html', contexto)

def area_remover(request, id):
    area = Area.objects.get(pk=id)
    area.delete()
    return redirect('areas')

def area_editar(request, id):
    area = Area.objects.get(pk=id)
    form = AreaForm(request.POST or None, instance=area)

    if form.is_valid():
        form.save()
        return redirect ('areas')

    contexto = {
        'form':form
    }

    return render(request, 'area_cadastro.html', contexto)