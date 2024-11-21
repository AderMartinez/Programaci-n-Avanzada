from django import forms
from .models import Reserva

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['mesa', 'cliente', 'fecha', 'hora', 'duracion', 'comentario']
