from django.urls import path
from .views import index, categorias
from .views import areas, area_cadastro, area_remover, area_editar
<<<<<<< HEAD
from .views import publicos, publico_cadastrar, publico_editar, publico_remover
from .views import perfil, autenticacao, desconectar
from .views import registro
=======
from .views import instrutor, instrutor_cadastro, instrutor_remover, instrutor_editar
from .views import publico

>>>>>>> e0f5687a5e823212a1eea974a2b359727c074cc1

urlpatterns = [

    path('perfil/', perfil, name='perfil'),
    path('login/', autenticacao, name='login'),
    path('desconectar/', desconectar, name='desconectar'),

    path('', index, name='index'),
    path('categorias/', categorias, name='categorias'),

    path('areas/', areas, name='areas'),
    path('area_cadastro/', area_cadastro, name='area_cadastro'),
    path('area_remover/<int:id>/', area_remover, name='area_remover'),
<<<<<<< HEAD
    path('area_editar/<int:id>/', area_editar,name='area_editar'),

    path('publicos/', publicos, name='publicos'),
    path('publico_cadastrar', publico_cadastrar, name='publico_cadastrar'),
    path('publico_remover/<int:id>/', publico_remover, name='publico_remover'),
    path('publico_editar/<int:id>', publico_editar, name='publico_editar'),
    path('cadastro/', registro, name='cadastro')

]
=======
    path('area_editar/<int:id>/', area_editar, name='area_editar'),
    path('instrutor/', instrutor, name='instrutor'),
    path('instrutor_remover/<int:id>/',instrutor_remover, name='instrutor_remover'),
    path('instrutor_editar/<int:id>/',instrutor_editar, name='instrutor_editar'),
    path('instrutor_cadastro/', instrutor_cadastro, name='instrutor_cadastro')
]
>>>>>>> e0f5687a5e823212a1eea974a2b359727c074cc1
