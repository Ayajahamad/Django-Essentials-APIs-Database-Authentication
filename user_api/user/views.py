from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, permission_classes, parser_classes


# Param for Swagger UI
photo_param = openapi.Parameter('photo', openapi.IN_FORM, description="Upload a photo", type=openapi.TYPE_FILE)
first_name_param = openapi.Parameter('first_name', openapi.IN_FORM, description="User's first name", type=openapi.TYPE_STRING)
last_name_param = openapi.Parameter('last_name', openapi.IN_FORM, description="User's last name", type=openapi.TYPE_STRING)
dob_param = openapi.Parameter('date_of_birth', openapi.IN_FORM, description="User's date of birth", type=openapi.TYPE_STRING,format='date')

# POST (create a new user)
@swagger_auto_schema(
    operation_description="Create a new user",
    manual_parameters=[first_name_param, last_name_param, dob_param, photo_param],
    methods=['POST']
)
@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])  # Allow multipart/form-data parsing
def create_user(request):
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        photo_data = None
        if photo:
            photo_data = photo.read()

        user = User.objects.create(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            date_of_birth=request.data['date_of_birth'],
            photo=photo,
            photo_data=photo_data
        )

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# GET (get all users)
@swagger_auto_schema(
    operation_description="Get all user details",
    methods=['GET']
)
@api_view(['GET'])
@permission_classes([AllowAny])
def get_users(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=200)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)


# GET (get a specific user by ID)
@swagger_auto_schema(
    operation_description="Get a single user by ID",
    methods=['GET']
)
@api_view(['GET'])
@permission_classes([AllowAny])
def get_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=200)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)


# GET (download user photo)
@swagger_auto_schema(
    operation_description="Download user photo by ID",
    methods=['GET']
)
@api_view(['GET'])
@permission_classes([AllowAny])
def download_user_photo(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if user.photo_data:
        try:
            response = HttpResponse(user.photo_data, content_type="image/jpeg")
            response['Content-Disposition'] = f'attachment; filename="{user.first_name}_photo.jpg"'
            return response
        except Exception as e:
            return Response({"error": f"Error serving binary photo: {str(e)}"}, status=500)
    return HttpResponse("User does not contain the Photo!")


# PUT (update an existing user)
@swagger_auto_schema(
    operation_description="Update an existing user",
    manual_parameters=[first_name_param, last_name_param, dob_param, photo_param],
    methods=['PUT']
)
@api_view(['PUT'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])  # Allow multipart/form-data parsing
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    photo = request.FILES.get('photo', None)
    photo_data = None

    if photo:
        photo_data = photo.read()

    user.first_name = request.data.get('first_name', user.first_name)
    user.last_name = request.data.get('last_name', user.last_name)
    user.date_of_birth = request.data.get('date_of_birth', user.date_of_birth)

    if photo:
        user.photo = photo
        user.photo_data = photo_data

    user.save()
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


# DELETE (delete a user by ID)
@swagger_auto_schema(
    operation_description="Delete a user by ID",
    methods=['DELETE']
)
@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
