from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from accounts.forms import RegisterForm
from accounts.models import MyUser


class LoginSiteView(LoginView):
    template_name = 'login.html'


class LogoutSiteView(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'


class RegisterUserView(CreateView):
    model = MyUser
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class FavoriteSkinsView(LoginRequiredMixin, ListView):
    template_name = 'profile.html'
    queryset = MyUser.objects.all()  # поменять на def get_queryset
