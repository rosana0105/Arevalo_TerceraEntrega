from django.shortcuts import render,redirect
from blogger.models import Blogger
from inicio.forms import CrearBlogFormulario,BuscarBlogFormulario

def inicio(request):
    return render(request, 'inicio/index.html')
   
def blog(request):
    formulario=BuscarBlogFormulario(request.GET)
    if formulario.is_valid():
        titulo=formulario.cleaned_data.get('titulo')
        blogs= Blogger.objects.filter(titulo__icontains=titulo)
    else:    
        blogs=Blogger.objects.all()

    return render(request, 'inicio/blog.html', {'blogs': blogs,'form':formulario})
    

def about_me(request):
    return render(request, 'inicio/acerca_de_mi.html')