from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class ContactUsuer(CreateView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Consulta enviada con exito.')
        return super().form_valid(form)
