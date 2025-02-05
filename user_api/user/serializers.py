from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'date_of_birth', 'photo']
        
    def get_photo_name(self, obj):
        if obj.photo:
            return obj.photo.name.split('/')[-1]  # Return just the file name
        return None  # Return None if no photo is uploaded
