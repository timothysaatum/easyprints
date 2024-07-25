from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML
from phonenumber_field.formfields import PhoneNumberField

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
    phone_number = PhoneNumberField(
        region='GH',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter a valid phone number (+233594438287)'
            }
        )
    )
    
    quantity = forms.IntegerField(
        initial=1,
        help_text='Enter number of codes you want to but E.g 10',
    )
    code_type = forms.ChoiceField(choices=CODE_TYPE)
    payment_mode = forms.ChoiceField(choices=MOMO_ACCOUNT_TYPE)

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            HTML(
                """
                <div class="input-group">
                    <div class="input-group-prepend">
                        <span class="input-group-text">+233</span>
                    </div>
                    {{form.phone_number}}
                </div>
            """)
        )


class RetrieveCodeForm(forms.Form):
    phone_number = PhoneNumberField(
        region='GH',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter a valid phone number (+233...)'
            }
        )
    )