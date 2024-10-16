from django.shortcuts import render,redirect
from inicio.models import Blog
from inicio.forms import CrearBlogFormulario,BuscarBlogFormulario

def inicio(request):
    return render(request, 'inicio/index.html')
   
def blog(request):
    formulario=BuscarBlogFormulario(request.GET)
    if formulario.is_valid():
        titulo=formulario.cleaned_data.get('titulo')
        blogs= Blog.objects.filter(titulo__icontains=titulo)
        print(blogs)
    else:    
        blogs=Blog.objects.all()
        print(blogs)

    return render(request, 'inicio/blog.html', {'blogs': blogs,'form':formulario})
    

def edicion(request):
    formulario=CrearBlogFormulario()
    if request.method=='POST':
        formulario=CrearBlogFormulario(request.POST)
        if formulario.is_valid():
            data=formulario.cleaned_data
            blog=Blog(titulo=data.get('titulo'), categoria=data.get('categoria'), anio=data.get('anio'))
            blog.save()
            return redirect ('inicio:blog')
    return render(request, 'inicio/edicion.html', {'form': formulario})

def about_me(request):
    return render(request, 'inicio/acerca_de_mi.html')