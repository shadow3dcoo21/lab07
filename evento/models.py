from django.db import models
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    organizador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='eventos_organizados')
    def __str__(self):
        return self.nombre
class RegistroEvento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='eventos_registrados')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='registros')
    def __str__(self):
        return self.usuario
# Create your models here.


