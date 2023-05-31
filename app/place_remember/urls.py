from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_memory/', views.add_memory, name='add_memory'),
]

