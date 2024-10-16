from django import forms

class CrearAutoFormulario(forms.Form):
    marca=forms.CharField(max_length=20)
    modelo=forms.CharField(max_length=20)
    anio=forms.IntegerField()
    
class BuscarAutoFormulario(forms.Form):
    marca=forms.CharField(max_length=20,required=False)
    
class CrearBlogFormulario(forms.Form):
    titulo=forms.CharField(max_length=20)
    categoria=forms.CharField(max_length=20)
    anio=forms.IntegerField()
    
class BuscarBlogFormulario(forms.Form):
    titulo=forms.CharField(max_length=20,required=False)
    