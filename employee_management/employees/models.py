from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField("name", max_length=50)
    email = models.EmailField("email", unique=True)
    department = models.CharField("department", max_length=50)
    joining_date = models.DateField("joining_date")
    
    def __str__(self):
        return f"Name :{self.name} and Email :{self.email}"