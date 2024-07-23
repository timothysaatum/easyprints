from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import FileUploadForm, TransactionForm
from django.urls import reverse_lazy
import pandas as pd
from .models import PinCode, Payment
import uuid
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .utils import SendSms,initialize_payment, verify_payment
from django.conf import settings



class MakePaymentView(TemplateView):
    template_name = 'main/index.html'


class UploadFileView(FormView):

    template_name = 'main/admin.html'
    form_class = FileUploadForm
    success_url = reverse_lazy('file-upload')

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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
        quantity = form.cleaned_data['quantity']
        code_type = form.cleaned_data['code_type']
        email = form.cleaned_data['email']
        pin_code = PinCode.objects.filter(code_type=form.cleaned_data['code_type'], is_used=False).first()

        code_sender = SendSms()
        recipients = [phone]

        message = f'Pin code:{pin_code.pin}, serial_number:{pin_code.serial_number}'
        sender = settings.SENDER_ID
        
        if pin_code:
            amount = pin_code.price * quantity
            reference = str(uuid.uuid4())
            initialize_payment(amount, email)
            code_sender.send_code(recipients, message, sender)
            Payment.objects.create(
                phone_number=phone, 
                amount=amount, 
                quantity=quantity, 
                reference=reference,
                code_type=code_type
            )
            verify_payment(reference)
            
        else:
            return JsonResponse({'message': 'Out of stock'})

        return redirect('home')
