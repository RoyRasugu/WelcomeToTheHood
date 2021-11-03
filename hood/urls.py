from django.urls import path
from hood import views

urlpatterns = [
    path('', views.home, name='home')
]