from django.db import models
from django.contrib.auth.models import User
from django.urls import path
from . import views

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    capasidad = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class booking(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    service = models.ForeignKey(Servicio, on_delete = models.CASCADE)
    fecha_reservacion = models.DateField()
    hora_reservacion = models.TimeField()
    guests = models.IntegerField()

    def __str__(self):
        return f"{self.usuario.username} - {self.service.nombre} - {self.fecha_reservacion} - {self.hora_reservacion} "

