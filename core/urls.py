from django.urls import path
from .views import index, categorias, areas
from .views import areas, area_cadastro

urlpatterns = [
    path('', index, name='index'),
    path('categorias/', categorias, name='categorias'),
    path('areas/', areas, name='areas'),
    path('area_cadastro/', area_cadastro, name='area_cadastro'),
]