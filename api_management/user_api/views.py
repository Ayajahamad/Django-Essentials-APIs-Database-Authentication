from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.generics import get_object_or_404
# from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework.response import Response

import logging

logger = logging.getLogger(__name__)

from .models import User, UserAddress, Bank, CompanyAddress, Hair, Company
from .serializers import (
    UserSerializer, 
    UserAddressSerializer, 
    HairSerializer, 
    CompanySerializer, 
    CompanyAddressSerializer,
    BankSerializer
)

# Home view
def home(request):
    return HttpResponse("Hello from user_api")

# User List and Create View
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"users": serializer.data})

    # def perform_create(self, serializer):
    #     serializer.save()
    
    # def get_queryset(self):
    #     return User.objects.all()
    
class UserListRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id' 
        

# User Address Create View
class UserAddressCreateView(generics.ListCreateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id'] 
        user = get_object_or_404(User, id=user_id)
        return UserAddress.objects.filter(user=user)
        
    def perform_create(self, serializer):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        
        # if UserAddress.objects.filter(user=user).exists():
        #     raise ValidationError({"detail": "A address already exists for this user."})
        
        serializer.save(user = user)
        


class UserAddressRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    http_method_names = ['get', 'put', 'delete']
    lookup_field = 'id'


# Hair Create View
class HairCreateView(generics.ListCreateAPIView):
    queryset = Hair.objects.all()
    serializer_class = HairSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id'] 
        user = get_object_or_404(User, id=user_id)
        return Hair.objects.filter(user=user)

    def perform_create(self, serializer):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        
        if Hair.objects.filter(user=user).exists():
            raise ValidationError({"detail": "A hair already exists for this user."})
        
        serializer.save(user=user)
        
class UserHairRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hair.objects.all()
    serializer_class = HairSerializer
    # http_method_names = ['get', 'put', 'delete']
    lookup_field = 'id'

# Bank Create View
class BankCreateView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id'] 
        user = get_object_or_404(User, id=user_id)
        return Bank.objects.filter(user=user)

    def perform_create(self, serializer):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
         
        # if Bank.objects.filter(user=user).exists():
        #     raise ValidationError({"detail": "A bank already exists for this user."})
        serializer.save(user=user)

class UserBankRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    # http_method_names = ['get', 'put', 'delete']
    lookup_field = 'id'
        

# Company Create View
class CompanyCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id'] 
        user = get_object_or_404(User, id=user_id)
        return Company.objects.filter(user=user)

    def perform_create(self, serializer):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        
        try:
            
            # if Company.objects.filter(user=user).exists():
            #     raise ValidationError({"detail": "A company already exists for this user."})
            serializer.save(user=user)
        
        except IntegrityError:
            raise ValidationError({"detail": "A company already exists for this user."})
        
class UserCompanyRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # http_method_names = ['get', 'put', 'delete']
    lookup_field = 'id'

# Company Address Create View
class CompanyAddressCreateView(generics.ListCreateAPIView):
    queryset = CompanyAddress.objects.all()
    serializer_class = CompanyAddressSerializer

    def get_queryset(self):
        com_id = self.kwargs['com_id'] 
        company = get_object_or_404(Company, id=com_id)
        return CompanyAddress.objects.filter(company=company)

    def perform_create(self, serializer):
        com_id = self.kwargs['com_id']
        company = get_object_or_404(Company, id=com_id) 
        
        # if CompanyAddress.objects.filter(company=company).exists():
        #     raise ValidationError("An address already exists for this company.")
        
        serializer.save(company=company)
        
class UserCompanyAddressRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyAddress.objects.all()
    serializer_class = CompanyAddressSerializer
    http_method_names = ['get', 'put', 'delete']
    lookup_field = 'id'
