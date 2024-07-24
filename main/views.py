from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import FileUploadForm, TransactionForm, RetrieveCodeForm
from django.urls import reverse_lazy
import pandas as pd
from .models import PinCode, Payment
import uuid
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .utils import SendSms,initialize_payment, verify_payment
from django.conf import settings
from decimal import Decimal



class RetrieveCode(FormView):
    template_name = 'main/index.html'


class UploadFileView(FormView):

    template_name = 'main/admin.html'
    form_class = FileUploadForm
    success_url = reverse_lazy('file-upload')

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

        phone = form.cleaned_data['phone_number']
        print(phone)
        quantity = form.cleaned_data['quantity']
        email = 'easyprintz@gmail.com'
        reference = str(uuid.uuid4())

        pin_code = PinCode.objects.filter(code_type=form.cleaned_data['code_type'], is_used=False).first()
        if pin_code:
            amount = Decimal(quantity) * pin_code.price
            try:
                initialize_payment(amount, email)
                verify_payment(reference)
                Payment.objects.create(
                    phone_number=phone, 
                    amount=amount, 
                    quantity=quantity,
                    email=email, 
                    reference=reference
                )
                code_sender = SendSms()
                recipients = [phone]

                message = f'Pin code:{pin_code.pin}, serial_number:{pin_code.serial_number}'
                sender = settings.SENDER_ID
                code_sender.send_code(recipients, message, sender)
            except Exception as e:
                print(e)

        return redirect('home')


class About(TemplateView):
    template_name = 'main/about.html'


class Services(TemplateView):
    template_name = 'main/services.html'