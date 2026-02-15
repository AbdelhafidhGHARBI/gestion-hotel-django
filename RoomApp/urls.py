from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
]
