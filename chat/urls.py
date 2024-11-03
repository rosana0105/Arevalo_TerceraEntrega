from django.urls import path
from chat.views import CrearChat

app_name = 'chat'

urlpatterns = [
    path('crear/<int:pk>/', CrearChat, name='crear_chat')
]
