# Django REST Framework uses serializers to convert data between Python objects and JSON format.

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password','user_type']