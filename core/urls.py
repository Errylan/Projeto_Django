from django.urls import path
from .views import index, categorias, areas
from .views import areas, area_cadastro, area_remover, area_editar
from .views import instrutor, indtrutor_cadastro, instrutor_remover, instrutor_editar

urlpatterns = [
    path('', index, name='index'),
    path('categorias/', categorias, name='categorias'),
    path('areas/', areas, name='areas'),
    path('area_cadastro/', area_cadastro, name='area_cadastro'),
    path('area_remover/<int:id>/', area_remover, name='area_remover'),
    path('area_editar/<int:id>/', area_editar, name='area_editar'),
    path('instrutor/', instrutor, name='instrutor'),
    path('instrutor_cadastro/', instrutor_cadastro, name='instrutor_cadastro'),
    path('instrutor_remover/<int:id>/', instrutor_remover, name='instrutor_remover'),
    path('instrutor_editar/<int:id>/', instrutor_editar, name='instrutor_editar'),
    

]