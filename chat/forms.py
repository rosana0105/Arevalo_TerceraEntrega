from django import forms
from chat.models import Chat

class CrearPostFormulario(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['comentario']
    