from django.urls import path
from inicio.views import inicio, blog, edicion, about_me

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('blog/', blog, name='blog'),
    path('edicion/', edicion, name='edicion'),
    path('aboutme/', about_me, name='acerca_de_mi')
]
