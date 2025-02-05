from django.urls import path
from . import views
from .views import UserListCreateView,UserAddressCreateView,CompanyAddressCreateView,CompanyCreateView,HairCreateView,BankCreateView, UserListRetrieveUpdateDeleteView,UserAddressRetrieveUpdateDeleteView,UserHairRetrieveUpdateDeleteView,UserCompanyRetrieveUpdateDeleteView,UserBankRetrieveUpdateDeleteView,UserCompanyAddressRetrieveUpdateDeleteView

urlpatterns = [
    path("", views.home, name='home'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:user_id>/address/', UserAddressCreateView.as_view(), name='user_address_create'),
    path('users/<int:user_id>/hair/', HairCreateView.as_view(), name='user_hair_create'),
    path('users/<int:user_id>/bank/', BankCreateView.as_view(), name='user_bank_create'),
    path('users/<int:user_id>/company/', CompanyCreateView.as_view(), name='user_company_create'),
    path('users/company/<int:com_id>/address/', CompanyAddressCreateView.as_view(), name='company_address_create'),
    
    # To update and delete
    path('users/<int:id>/', UserListRetrieveUpdateDeleteView.as_view(), name='user-list-update'),
    # path('users/<int:user_id>/address/', UserAddressRetrieveUpdateDeleteView.as_view(), name='user_address_update_delete'),
    path('users/<int:user_id>/address/<int:id>/', UserAddressRetrieveUpdateDeleteView.as_view(), name='user_address_update_delete'),
    path('users/<int:user_id>/hair/<int:id>/', UserHairRetrieveUpdateDeleteView.as_view(), name='user_hair_update_delete'),
    path('users/<int:user_id>/company/<int:id>/', UserCompanyRetrieveUpdateDeleteView.as_view(), name='user_company_update_delete'),
    path('users/<int:user_id>/bank/<int:id>/', UserBankRetrieveUpdateDeleteView.as_view(), name='user_bank_update_delete'),
    
    path('users/company/<int:com_id>/address/<int:id>', UserCompanyAddressRetrieveUpdateDeleteView.as_view(), name='company_address_update_delete_create'),
    


]
