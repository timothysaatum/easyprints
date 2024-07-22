from django.urls import path
from .views import IndexView, UploadFileView, MakePaymentView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('upload-document/', UploadFileView.as_view(), name='file-upload'),
    path('make-payment/', MakePaymentView.as_view(), name='make-payment')
]