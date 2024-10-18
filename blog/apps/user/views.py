
from .forms import RegForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

from django.views import View
from django.contrib.auth import logout

# Create your views here.

class RegisterUser(CreateView):
    template_name = 'registration/register.html'
    form_class = RegForm

    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso. Por favor, inicia sesión.')
        form.save()
        return redirect('apps.user:register')

class LoginUsuario(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login exitoso')
        return reverse('index')

# class LogoutUsuario(LogoutView):
#     template_name = 'registration/logout.html'

#     def get_success_url(self):
#         messages.success(self.request, 'Logout exitoso')
#         return reverse('apps.user:register')

class LogoutUsuario(View):
    def get(self, request):
        logout(request)
        return redirect('index')