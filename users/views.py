from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CustomUser


class AccountLocked(TemplateView):
    template_name = "users/account_locked.html"


class UserList(LoginRequiredMixin, ListView):
    template_name = "users/users_list.html"
    model = CustomUser
    context_object_name = "obj"