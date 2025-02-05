from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('register/',views.register,name='register'),
    path('login_page/',views.login_page,name='login_page'),
    path('login/',views.login_view, name='login'),
    path('student_dashboard/',views.student_dashboard, name='student_dashboard'),
    path('teacher_dashboard/',views.teacher_dashboard, name='teacher_dashboard'),
    path('reset_password/',views.reset_password, name='reset_password'),
    path('set_password/',views.set_password, name='set_password'),
    
    
    
    
    path("", views.home, name='home'),
    path('user/', views.UserList.as_view(), name='user_list'),
    path('user/<int:pk>/',views.UserDetail.as_view(), name='user_detail'),
    path('user/<str:username>/',views.UserDetailName.as_view(), name='user_detail_name'),
]