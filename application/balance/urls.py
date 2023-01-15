from django.urls import path
from balance import views

urlpatterns = [
    path('account_balance', views.accounts_balance_get),
]