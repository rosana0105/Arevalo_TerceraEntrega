from django.urls import path
from inicio.views import inicio, blog, about_me

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('blog/', blog, name='blog'),
    path('aboutme/', about_me, name='acerca_de_mi')
]
