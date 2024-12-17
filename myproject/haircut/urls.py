from django.urls import path
from .views import *
urlpatterns = [
    path("",firstpage,name="firstpage"),
    path("login/",login,name="login")
]
