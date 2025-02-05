# models.py
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True) # files will be saved in the "MEDIA_ROOT/user_photos/" directory
    photo_data = models.BinaryField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
