from django import forms

CODE_TYPE = [
    ('WASSCE, OLD WASSCE, SSCE', 'WASSCE, OLD WASSCE, SSCE'),
    ('BECE', 'BECE'),
    ('SHS PLACEMENT CODES', 'SHS PLACEMENT CODES')

]
QUANTITY = [
    ('10 pin @ 18ghs', '10 pin @ 18ghs')
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
    pnone_number = forms.CharField(max_length=10)
    quantity = forms.ChoiceField(choices=QUANTITY)
    code_type = forms.ChoiceField(choices=CODE_TYPE)
    payment_mode = forms.ChoiceField(choices=MOMO_ACCOUNT_TYPE)
