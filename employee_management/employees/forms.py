from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'department', 'joining_date']


# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = ['name', 'email', 'department', 'joining_date']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Enter your name'}),
#             'email': forms.EmailInput(attrs={'class': 'custom-input', 'placeholder': 'Enter your email'}),
#             'department': forms.TextInput(attrs={'class': 'custom-input', 'placeholder': 'Enter department name'}),
#             'joining_date': forms.DateInput(attrs={'class': 'custom-input', 'type': 'date'}),
#         }
