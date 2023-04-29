from django.urls import path

from .views import get_users_list, get_user

urlpatterns = [
    path('users/', get_users_list, name='users'),
    path('user/<int:pk>', get_user, name='user')
]
