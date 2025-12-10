from . import views
from django.urls import path

app_name='subjects'

urlpatterns = [
    path('',views.subject_list,name='subject-list')
]
