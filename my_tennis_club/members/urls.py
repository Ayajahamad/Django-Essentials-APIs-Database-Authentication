from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<slug:slug>', views.deatils, name='deatils'),
    path('testing/', views.testing, name='testing'),
]