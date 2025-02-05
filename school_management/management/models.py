from django.db import models

# A simple user model for login and registration
class User(models.Model):
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Password field for login
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')
    
    def __str__(self):
        return self.username


# Student Model
class Student(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)  # Linking Student to User
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.TextField()
    branch = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Teacher Model
class Teacher(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)  # Linking Teacher to User
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    hire_date = models.DateField()
    address = models.TextField()
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Attendance Model (Connected to Student)
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Linking Attendance to Student
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"

