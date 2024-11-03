from django.db import models
from django.contrib.auth.models import User
from blogger.models import Blogger

class Chat(models.Model):
    comentario = models.CharField(max_length=50)
    fecha = models.DateField()
    blog = models.ForeignKey(Blogger, on_delete=models.CASCADE, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id} {self.comentario}'

