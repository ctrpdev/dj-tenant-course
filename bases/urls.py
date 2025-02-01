from django.urls import path, include
from .views import *

app_name = "bases"

urlpatterns = [
    path("", Home.as_view(), name="home"),
]