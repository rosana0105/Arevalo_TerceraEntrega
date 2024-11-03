from django.urls import path
from blogger import views

app_name = 'blogger'

urlpatterns = [
    path('crear/', views.CrearBlogger.as_view(), name='crear_blogger'),
    path('listado/', views.ListadoBlogger.as_view(), name='listado_blogger'),
    path('ver/<int:pk>/', views.VerBlogger.as_view(), name='ver_blogger'),
    path('editar/<int:pk>/', views.EditarBlogger.as_view(), name='editar_blogger'),
    path('eliminar/<int:pk>/', views.EliminarBlogger.as_view(), name='eliminar_blogger'),
    path('vermas/<int:pk>/', views.VerMasBlogger.as_view(), name='vermas_blogger'),
]
