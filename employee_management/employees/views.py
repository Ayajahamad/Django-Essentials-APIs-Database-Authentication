from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

# Create an Employee
def create_employee(request):
    if request.method == 'POST':
        # 'request.POST': This is a dictionary-like object containing all the form data submitted by the user.
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # If the form is valid, this line 'form.save()' saves the data to the database. The save() method is automatically provided by Django when you use ModelForm, and it saves a new instance of the Employee model using the data from the form.
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/create_employee.html', {'form': form})


# Show all Employees
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

# Update an Employee
def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        # 'instance=employee' ensures that the existing employee record is pre-filled with the current values from the database.
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/update_employee.html', {'form': form})

# Delete an Employee
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/delete_employee.html', {'employee': employee})

