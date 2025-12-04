from django import forms
from .models import Area, Publico, Instrutor, Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta :
        model = Usuario
        fields =['cpf',
        'nome_completo',
        'email',
        'password1',
        'password2']

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome']

class PublicoForm(forms.ModelForm):
    class Meta:
        model = Publico
        fields = ['nome']

class InstrutorForm(forms.ModelForm):
    class Meta:
        model = Instrutor
        fields = ['nome']