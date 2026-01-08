from django.urls import path, register_converter

from . import converters, views

app_name = 'users'

register_converter(converters.ProfileConverter, 'profile')

urlpatterns = [
    path('user/edit/', views.user_edit, name='edit-profile'),
    path('user/leave/', views.user_leave, name='delete-profile'),
    path('users/<profile:profile>/', views.user_detail, name='profile-detail'),
]
