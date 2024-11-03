from django.db import models

class Blog(models.Model):
    titulo = models.CharField(max_length=40)
    categoria = models.CharField(max_length=20)
    anio = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} {self.categoria} {self.anio}'