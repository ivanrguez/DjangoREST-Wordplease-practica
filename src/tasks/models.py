from django.contrib.auth.models import User
from django.db import models

from django.conf import settings


class Categorias(models.Model):

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Post(models.Model):

    PUBLICO = 'PUB'
    PRIVADO = 'PRI'
    Estado = (
        (PUBLICO, 'Publico'),
        (PRIVADO, 'Privado')
    )


    categoria = models.ManyToManyField(Categorias)
    titulo = models.CharField(max_length=100)
    intro = models.TextField()
    descripcion = models.TextField()
    imagen = models.URLField()
    user = models.ForeignKey(User, related_name='user_post')
    deadline = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=3, default=PUBLICO, choices=Estado)


    def __str__(self):
        return self.titulo


