from django.urls import path
from .views import index, categorias

urlpatterns = [
    path('', index, name='index'),
    path('categorias/', categorias, name='categorias'),
]