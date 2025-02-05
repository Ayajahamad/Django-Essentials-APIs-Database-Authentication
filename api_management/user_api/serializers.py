from rest_framework import serializers
from .models import User, UserAddress, Bank, CompanyAddress, Hair, Company

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['id', 'city', 'state', 'post_code', 'country']
        
class HairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hair
        fields = ['id', 'color', 'type']
        
class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'card_number', 'card_type', 'currency', 'iban']
        
class CompanyAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAddress
        fields = ['id', 'address', 'city', 'state', 'country']
        
class CompanySerializer(serializers.ModelSerializer):
    address = CompanyAddressSerializer(many=True ,read_only=True)
    
    class Meta:
        model = Company
        fields = ['id', 'department', 'name', 'title', 'address']
        
class UserSerializer(serializers.ModelSerializer):
    address = UserAddressSerializer(many=True , read_only=True)
    hair = HairSerializer(read_only=True) 
    bank = BankSerializer(many=True ,read_only=True)
    company = CompanySerializer(many=True ,read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'age', 'birth_date', 'address', 'hair', 'bank', 'company']
