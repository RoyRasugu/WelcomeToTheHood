from django.urls import path
from hood import views

urlpatterns = [
    path('', views.registration, name='registration'),
    path('home', views.home, name='home')
]