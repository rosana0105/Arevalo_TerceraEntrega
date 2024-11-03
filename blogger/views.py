from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blogger.models import Blogger
from django.contrib.auth.models import User
from usuarios.models import DatosAdicionales
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from chat.forms import CrearPostFormulario
from django.shortcuts import get_object_or_404

# Create your views here.
class CrearBlogger(LoginRequiredMixin, CreateView):
    model = Blogger
    template_name = "blogger/crear_blogger.html"
    success_url = reverse_lazy('blogger:listado_blogger')
    fields = ['titulo', 'categoria', 'fecha', 'descripcion', 'autor', 'image_blog']
    
class ListadoBlogger(ListView):
    model = Blogger
    template_name = "blogger/listado_blogger.html"
    context_object_name = 'bloggers'

class VerBlogger(LoginRequiredMixin, DetailView):
    model = Blogger
    template_name = "blogger/ver_blogger.html"

class EditarBlogger(LoginRequiredMixin, UpdateView):
    model = Blogger
    template_name = "blogger/editar_blogger.html"
    success_url = reverse_lazy('blogger:listado_blogger')
    fields = ['titulo', 'categoria', 'fecha', 'descripcion', 'autor', 'image_blog']

class EliminarBlogger(LoginRequiredMixin, DeleteView):
    model = Blogger
    template_name = "blogger/eliminar_blogger.html"
    success_url = reverse_lazy('blogger:listado_blogger')

class VerMasBlogger(LoginRequiredMixin, FormMixin, DetailView):
    model = Blogger
    form_class = CrearPostFormulario
    template_name = "blogger/vermas_blogger.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chats = self.object.chat_set.all()
        comentarios = []
        for chat in  chats:
            user = get_object_or_404(User, pk=chat.usuario.id)
            url = get_object_or_404(DatosAdicionales, user=user).avatar.url 
        
            comentarios.append({
                'id': chat.id,
                'comentario': chat.comentario,
                'fecha': chat.fecha,
                'username': user.username,
                'imagen': url
            })

        context['chats'] = comentarios
        return context