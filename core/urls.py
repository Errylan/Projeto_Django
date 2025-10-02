from django.urls import path
from .views import index, categorias, areas

urlpatterns = [
    path('', index, name='index'),
    path('categorias/', categorias, name='categorias'),
    path('areas/', areas, name='areas'),
]