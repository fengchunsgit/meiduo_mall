from django.contrib import admin
from django.urls import path, include
# from .views import RegisterView
from . import views
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register")
]