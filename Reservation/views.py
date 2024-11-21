from django.shortcuts import render, redirect
from .models import Reserva, Mesa  # Modelo de reserva Y TABLAS
from .forms import ReservationForm  # Formulario para crear reservas
from django.contrib import messages #para mostrar un mensaje de exito o error
# Vista para listar todas las reservas
def reservacion_view(request):
   reservaciones = Reserva.objects.all().order_by("fecha","hora")  # Obtiene todas las reservas
   return render(request, 'reservation_list.html', {'reservaciones': reservaciones})

# Vista para crear una nueva reserva
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
             # Obtener datos del formulario
            date = form.cleaned_data['fecha']
            time = form.cleaned_data['hora']
            table = form.cleaned_data['mesa']

            existing_reservation = Reserva.objects.filter(fecha=date, hora=time, mesa=table).exists()
  
        if existing_reservation:
                messages.error(request,"La mesa ya está reservada en ese horario") 
        else: 
             # Lógica de negocio para verificar disponibilidad o datos
              form.save()  # Guarda la nueva reserva
              messages.success(request, 'Reservacion creada con exitos')
              return redirect('reservacion_list')  # Redirige a la lista de reservas
    else:
        form = ReservationForm()  # Formulario vacío para GET
    return render(request, 'reservaciones/create_reservation.html', {'form': form})
