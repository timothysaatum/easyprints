from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import FileUploadForm, TransactionForm
from django.urls import reverse_lazy
import pandas as pd
from .models import PinCode, Payment
import uuid
from django.contrib.auth.mixins import LoginRequiredMixin


class MakePaymentView(TemplateView):
    template_name = 'main/index.html'


class UploadFileView(FormView):

    template_name = 'main/admin.html'
    form_class = FileUploadForm
    sucess_url = reverse_lazy('file-upload')

    def form_valid(self, form):

        file = form.cleaned_data['file']
        documnet_type = form.cleaned_data['document_type']
        df = pd.read_excel(file)

        for _, row in df.iterrows():
            pin, serial = row
            PinCode.objects.create(code_type=documnet_type,pin=pin, serial_number=serial)

        return super().form_valid(form)


class IndexView(FormView):

    form_class = TransactionForm
    template_name = 'main/index.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        phone = form.cleaned_data['pnone_number']
        amount = 10000
        reference = str(uuid.uuid4())
        Payment.objects.create(phone_number=phone, amount=amount, reference=reference)

        return redirect('home')