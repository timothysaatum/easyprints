from django.urls import path
from .views import IndexView, AdminView, RetrieveCode, About, Services

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('easyprintz/admin/', AdminView.as_view(), name='admin'),
    path('retrieve-code/', RetrieveCode.as_view(), name='retrieve-code'),
    path('about/', About.as_view(), name='about'),
    path('services/', Services.as_view(), name='services'),
]