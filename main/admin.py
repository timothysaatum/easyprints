from django.contrib import admin
from .models import PinCode, Payment


class PinCodeAdmin(admin.ModelAdmin):
    list_display = [
        'code_type',
        'pin',
        'serial_number',
        'is_used'
    ]


class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        'phone_number',
        'amount',
        'reference',
        'is_successful'
    ]


admin.site.register(PinCode, PinCodeAdmin)
admin.site.register(Payment, PaymentAdmin)