# from django.contrib import admin
# from .models import User, Student, Teacher, Attendance

# admin.site.register(User)
# admin.site.register(Student)
# admin.site.register(Teacher)
# admin.site.register(Attendance)


from django.contrib import admin
from django import forms
from .models import User, Student, Teacher, Attendance

# Custom form for Student
class StudentAdminForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit the 'user' field to users with 'student' role only
        self.fields['user'].queryset = User.objects.filter(user_type='student')

# Custom Admin for Student to use the custom form
class StudentAdmin(admin.ModelAdmin):
    form = StudentAdminForm

# Custom form for Teacher
class TeacherAdminForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit the 'user' field to users with 'teacher' role only
        self.fields['user'].queryset = User.objects.filter(user_type='teacher')

# Custom Admin for Teacher to use the custom form
class TeacherAdmin(admin.ModelAdmin):
    form = TeacherAdminForm

# Register models in the admin interface
admin.site.register(User)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Attendance)

