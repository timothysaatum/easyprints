from django.urls import path
from .views import IndexView, UploadFileView, RetrieveCode, About, Services

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('upload-document/', UploadFileView.as_view(), name='file-upload'),
    path('retrieve-code/', RetrieveCode.as_view(), name='retrieve-code'),
    path('about/', About.as_view(), name='about'),
    path('services/', Services.as_view(), name='services'),
]