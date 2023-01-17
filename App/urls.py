# write your urls here

from django.urls import path
from . import views

urlpatterns=[
    path('', views.registration, name="register")
]