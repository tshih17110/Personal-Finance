from django.urls import path
from transaction import views

urlpatterns = [
    path('get_transactions', views.get_transactions),
]