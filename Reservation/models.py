from django.db import models

# Create your models here.
class Mesa(models.Model):
    numero = models.IntegerField(unique=True) #Númerode las mesas
    capacidad = models.IntegerField()  #Capacidad de personas
    ubicacion = models.CharField(max_length=100, blank = True)
    
    
    def __str__(self):
        return f" Mesa: {self.numero}, Capacidad: {self.capacidad}"
    
    
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank = True, null = True)
    
    
    def __str__(self):
        return self.nombre
    
    
class Reserva(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE) #Relación con la mesa
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) #Relación con el cliente
    fecha = models.DateField() #Fechad e la reserva
    hora = models.TimeField() #Hora de la reserva
    duracion =models.IntegerField(default=2) #duración en horas
    comentario = models.TextField(blank=True) #Notas Adicionales
    
    class Meta:
     constraints = [
        models.UniqueConstraint(fields=['mesa', 'fecha', 'hora'], name='unique_reserva')
    ]

        
    def __str__(self):
        return f"Reserva de {self.cliente.nombre} en la Mesa {self.mesa.numero} el {self.fecha} a las {self.hora}"
    
