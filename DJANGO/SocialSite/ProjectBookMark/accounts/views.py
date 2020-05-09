from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import MyUserCreationForm
# Create your views here.

class MyLoginView(LoginView):
  template_name = 'login.html'

class MyLogoutView(LogoutView):
  template_name = 'logout.html'

class MyUserCreationView(SuccessMessageMixin, CreateView):
  template_name = 'signup.html'
  form_class = MyUserCreationForm
  success_url = reverse_lazy('accounts:login')
  success_message = 'Welcome aboard! Please login to continue!'