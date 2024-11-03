from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class FormularioDeCreacionDeUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contrasenia', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    fecha_nacimiento = forms.DateField(label='Fecha Nacimiento')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'fecha_nacimiento', 'password1', 'password2']
        help_texts = {key: '' for key in fields}
        
class FormularioEdicionPerfil(UserChangeForm):
    email = forms.EmailField(label='Correo electronico')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password = None
    avatar = forms.ImageField(required=False)
    fecha_nacimiento = forms.DateField(label='Fecha Nacimiento')
    
    class Meta():
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar', 'fecha_nacimiento']