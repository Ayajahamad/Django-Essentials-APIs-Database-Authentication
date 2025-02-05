import json
from django.http import  HttpResponse
from django.contrib.auth.hashers import make_password

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'management/index.html')

def register(request):
    return render(request, 'management/register.html')

def login_page(request):
    return render(request, 'management/login.html')

def student_dashboard(request):
    return render(request, 'management/student_dashboard.html')

def teacher_dashboard(request):
    return render(request, 'management/teacher_dashboard.html')

def reset_password(request):
    return render(request, 'management/reset_password.html')

# Login using username and password
# @csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        print(f"Received data: {data}")

        try:
            user = User.objects.get(username=username)
            print(user.email)
            # user = User.objects.get(username=username) and User.objects.get(password=password)
            if user and user.password == password and user.user_type == 'student':
                # login(request, user)
                return JsonResponse({'success': True,'redirect': '/management/student_dashboard/','role':'student'})
            
            if user and user.password == password and user.user_type == 'teacher':
                return JsonResponse({'success': True,'redirect': '/management/teacher_dashboard/','role':'teacher'})
            
            else:
                return JsonResponse({'success': False, 'message': 'Invalid credentials'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User does not exist'}, status=401)

    return JsonResponse({'message': 'Method not allowed'}, status=405)

# Reset the password using username
def set_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        new_password = data.get('new_password')

        print(f"Received data: {data}")

        try:
            user = User.objects.get(username=username)
            # user.password = make_password(new_password) # with hashing
            user.password = new_password
            user.save()
            return JsonResponse({'success': True, 'message': 'Password updated successfully'})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User does not exist'}, status=404)

    return JsonResponse({'message': 'Method not allowed'}, status=405)
    

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserDetailName(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)