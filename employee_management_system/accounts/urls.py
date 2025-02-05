from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.home, name='home'),
    path("login/", views.login_view, name='login'),
    path("register/", views.register_view, name='register'),
    path("reset_password/", views.password_reset_view, name="reset"),
    path("logout/",views.logout_view, name='logout'),
    path("user/", views.user, name='user'),
    path("admin/",views.admin, name='admin')
]