import africastalking
from django.conf import settings
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Payment



class SendSms:

    def __init__(self) -> None:

        self.username = settings.USERNAME
        self.api_key = settings.API_KEY
        africastalking.initialize(self.username, self.api_key)
        self.sms = africastalking.SMS

    def send_code(self, recipients, message, sender):

        try:
            response = self.sms.send(message, recipients, sender)
            # print(response)
            return response

        except Exception as e:
            print(e)


headers = {
        'Authorization': f'Bearer {settings.PAYSTACK_TEST_SECRET}',
        'Content-Type': 'application/json'
    }

@csrf_exempt
def verify_payment(reference):

    response = requests.get(f'https://api.paystack.co/transaction/verify/{reference}', headers=headers)
    response_data = response.json()
    # print(response_data)
    if response_data['status']:
        pay = Payment.objects.get(reference=reference)
        if response_data['data']['status'] == 'success':
            pay.is_successful = True
            pay.save()
            return JsonResponse({'message': 'Payment verified successfully'})

        return JsonResponse({'message': 'Verification failed'})

    else:
        return JsonResponse({'message': response_data['message']})

def initialize_payment(amount, email, reference):
    amount = int(amount) * 100

    data = {
        'email': email,
        'amount': amount,
        'currency': 'GHS',
        'channels': ['mobile_money', 'ussd']
    }

    response = requests.post('https://api.paystack.co/transaction/initialize', headers=headers, json=data)
    response_data = response.json()
    print(response_data)
    if response_data['status']:
        authorization_url = response_data['data']['authorization_url']
        reference = response_data['data']['reference']
        verify_payment(reference)
        # print(authorization_url, reference)
        # Payment.objects.create()
        return JsonResponse(response_data['data'])

    else:
        return JsonResponse(response_data['data'])
