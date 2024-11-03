from django.db import models
from django.contrib.auth.models import User

class DatosAdicionales(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', blank=True, null=True, default='avatares/default.jpg')
    fecha_nacimiento = models.DateField()
    