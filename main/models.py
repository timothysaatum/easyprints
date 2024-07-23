from django.db import models

CODE_TYPE = [
    ('WASSCE, OLD WASSCE, SSCE', 'WASSCE, OLD WASSCE, SSCE'),
    ('BECE', 'BECE'),
    ('SHS PLACEMENT CODES', 'SHS PLACEMENT CODES')

]

class PinCode(models.Model):
    code_type = models.CharField(max_length=100, choices=CODE_TYPE)
    pin = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.code_type


class Payment(models.Model):

    phone_number = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=100, unique=True)
    is_successful = models.BooleanField(default=False)

    def __str__(self):
        return self.phone_number