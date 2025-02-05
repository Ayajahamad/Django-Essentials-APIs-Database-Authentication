from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = 'login_loguot/login.html'
    authentication_form = UserLoginForm  # Here, the custom form is explicitly assigned.


    def get_success_url(self):
        print(f"User: {self.request.user.role}")
        print(f"is_active: {self.request.user.is_active}")
        print(f"is_staff: {self.request.user.is_staff}")
        print(f"is_superuser: {self.request.user.is_superuser}")
        if self.request.user.role == 'admin':
            return reverse_lazy('admin_dashboard')
        return reverse_lazy('user_dashboard')


@login_required
def admin_dashboard(request):
    return render(request, 'login_loguot/admin_dashboard.html')

@login_required
def user_dashboard(request):
    return render(request, 'login_loguot/user_dashboard.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')  # Redirect to the login page
    else:
        form = UserRegistrationForm()
    return render(request, 'login_loguot/register.html', {'form': form})
