from rest_framework.routers import DefaultRouter
from django.urls import path

from finance import views

urlpatterns = [
    path('create_link_token', views.create_link_token),
]
