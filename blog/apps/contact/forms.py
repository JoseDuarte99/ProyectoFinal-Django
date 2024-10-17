from django import forms
from .models import Contact
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'subject', 'message']  # nombre_apellido, asunto, mensaje
        labels = {
            'full_name': _('Nombre y Apellido'),
            'email': _('Correo Electrónico'),
            'subject': _('Asunto'),
            'message': _('Mensaje'),
        }