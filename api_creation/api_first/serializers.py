# Django REST Framework uses serializers to convert data between Python objects and JSON format.

from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','description','complete']