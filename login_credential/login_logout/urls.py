# urls.py
from django.urls import path
from .views import CustomLoginView, admin_dashboard, user_dashboard, register

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('user/dashboard/', user_dashboard, name='user_dashboard'),
    path('register/', register, name='register'),
    
]
