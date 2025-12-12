from . import views
from django.urls import path, register_converter
from . import converters


app_name = 'users'
register_converter(converters.ProfileConverter,'profile')
urlpatterns = [
    path('<profile:profile>/', views.user_detail, name='profile-detail'),
    path('edit/', views.user_edit, name='profile-edit'),
    path('leave/', views.user_leave, name='profile-leave'),


]
