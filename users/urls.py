from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

app_name = "users"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/login.html'), name='logout'),
    path('account-locked/', AccountLocked.as_view(), name='account_locked'),
    path('users/list/', UserList.as_view(), name='users_list'),
]