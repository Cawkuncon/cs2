from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView, DetailView, TemplateView

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

    def post(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, message='User has been registered successfully')
        return super().post(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'


class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('profile')


class DeleteUser(LoginRequiredMixin, DeleteView):
    """почему так???"""
    model = MyUser
    template_name = 'delete_user.html'
    success_url = reverse_lazy('register')

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, message='User has been deleted successfully')
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)
