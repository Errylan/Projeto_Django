from django.shortcuts import render, redirect
from .models import Area, Instrutor, Publicos
from .forms import AreaForm, InstrutorForm, PublicoForm

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

def  publicos(request):
    publicos = Publicos.objects.all()
    contexto ={
        'lista_publicos': publicos
    }
    return render (request, 'publicos.html', contexto)

def publicos_cadastro(request):
    form = PublicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('publicos')



    contexto ={
        'form' :form
    }
    return render(request, 'publico_cadastro.html', contexto)

def publicos_remover(request, id):
    publicos = Publicos.objects.get(pk=id)
    publicos.delete()
    return redirect('publicos')

def publicos_editar(request, id):
    area = Publicos.objects.get(pk=id)
    form = PublicoForm(request.POST or None, instance=publicos)

    if form.is_valid():
        form.save()
        return redirect ('publicos')

    contexto = {
        'form':form
    }

    return render(request, 'publico_cadastro.html', contexto)

def  instrutor(request):
    instrutor = Instrutor.objects.all()
    contexto ={
        'lista_instrutor': instrutor
    }
    return render (request, 'instrutor.html', contexto)

def instrutor_cadastro(request):
    form = InstrutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('instrutor')



    contexto ={
        'form' :form
    }
    return render(request, 'instrutor_cadastro.html', contexto)

def instrutor_remover(request, id):
    instrutor = instrutor.objects.get(pk=id)
    instrutor.delete()
    return redirect('instrutor')

def instrutor_editar(request, id):
    area = Instrutor.objects.get(pk=id)
    form = InstrutorForm(request.POST or None, instance=instrutor)

    if form.is_valid():
        form.save()
        return redirect ('instrutor')

    contexto = {
        'form':form
    }

    return render(request, 'instrutor_cadastro.html', contexto)