from django.urls import path
from .views import create_user, get_users, get_user, download_user_photo, update_user, delete_user

# for swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your-email@domain.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # patterns=[
    #     path('create_user/', create_user, name='post_user')
    # ]
)


urlpatterns = [
    # path("", home, name='home'),
    path("create_user/", create_user, name='post_user'),
    path("get_users/", get_users, name='get_users'),
    path("get_user/<int:user_id>/", get_user, name="get_user"),
    path("update_user/<int:user_id>/", update_user, name="update_user"),
    path("delete_user/<int:user_id>/", delete_user, name="delete_user"),
    path("get_user/<int:user_id>/photo/", download_user_photo, name="download_user_photo"),

    # For Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
]
