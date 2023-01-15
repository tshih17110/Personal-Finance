from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path('', TemplateView.as_view(template_name='frontend/index.html')),
    path('finance', TemplateView.as_view(template_name='frontend/finance.html')),
    path('authentication/', include('authentication.urls')),
    path('finance/balance/', include('balance.urls')),
]