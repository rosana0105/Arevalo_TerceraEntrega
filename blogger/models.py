from django.db import models

class Blogger(models.Model):
    titulo = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    fecha = models.DateField()
    descripcion = models.TextField()
    autor = models.CharField(max_length=30)
    image_blog = models.ImageField(upload_to='blogger', blank=True, null=True)
    
    def __str__(self):
        return f'{self.id} {self.titulo}'
