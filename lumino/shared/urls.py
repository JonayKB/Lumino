from django.urls import path

import shared.views as views

urlpatterns = [
    path('', views.index, name='index'),
]
