from datetime import datetime
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from chat.models import Chat
from blogger.models import Blogger
from chat.forms import CrearPostFormulario
from django.contrib.auth.models import User

# Create your views here.
@login_required
def listar_chats(request):
    datos_extra = request.user    
    return render(request, 'usuarios/ver_perfil.html', {'form': datos_extra})

@login_required
def CrearChat(request, pk):
    if request.method == "POST":
        formulario=CrearPostFormulario(request.POST)
        if formulario.is_valid():
            blog = get_object_or_404(Blogger, pk=pk)
            fecha_actual = datetime.now()
            user = get_object_or_404(User, pk = request.user.id)
            data=formulario.cleaned_data
            chat = Chat(
                comentario=data.get("comentario"),
                fecha=fecha_actual.strftime("%Y-%m-%d"),
                blog = blog,
                usuario=user
            )
            chat.save()
            return redirect('blogger:vermas_blogger', pk=blog.pk)
            