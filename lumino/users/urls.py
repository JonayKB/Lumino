from . import views
from django.urls import path, register_converter
from . import converters


app_name = 'users'
register_converter(converters.ProfileConverter,'profile')
urlpatterns = [
    path('<profile:username>/', views.user_detail, name='profile-detail'),
]
