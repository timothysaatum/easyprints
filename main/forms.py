from django import forms

CODE_TYPE = [
    ('WASSCE', 'WASSCE'),
    ('BECE', 'BECE'),
    ('SHS PLACEMENT CODES', 'SHS PLACEMENT CODES')
]

MOMO_ACCOUNT_TYPE = [
    ('Telecel cash', 'Telecel cash'),
    ('MTN cash', 'MTN cash'),
    ('Airtel cash', 'Airtel cash')
]
class FileUploadForm(forms.Form):
    file = forms.FileField()
    document_type = forms.ChoiceField(choices=CODE_TYPE)


class TransactionForm(forms.Form):
    phone_number = forms.CharField(max_length=15)
    email = forms.EmailField()
    quantity = forms.DecimalField(max_digits=10, decimal_places=2)
    code_type = forms.ChoiceField(choices=CODE_TYPE)
    payment_mode = forms.ChoiceField(choices=MOMO_ACCOUNT_TYPE)
