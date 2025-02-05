from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('task/',views.task, name='task'),
    path('tasks/', views.TaskList.as_view(), name='task_list'),
    path('tasks/<int:pk>/',views.TaskDetail.as_view(), name='task_detail'),
]