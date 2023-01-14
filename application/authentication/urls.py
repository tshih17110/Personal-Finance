from rest_framework.routers import DefaultRouter
from django.urls import path

from authentication import views

urlpatterns = [
    path('create_link_token', views.create_link_token),
    path('exchange_public_token', views.exchange_public_token),

]
