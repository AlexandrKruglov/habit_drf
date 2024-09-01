from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from users.apps import UsersConfig
from users.views import UserListAPIView, UserCreateAPIView, UserUpdateAPIView, UserRetrieveAPIView, UserDestroyAPIView


app_name = UsersConfig.name

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='users_list'),
    path('users/create/', UserCreateAPIView.as_view(), name='users_create'),
    path('users/<int:pk>/update/', UserUpdateAPIView.as_view(), name='users_update'),
    path('users/<int:pk>/', UserRetrieveAPIView.as_view(), name='users_retrieve'),
    path("users/<int:pk>/delete/", UserDestroyAPIView.as_view(), name="users-delete"),
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    ]
