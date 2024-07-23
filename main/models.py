from django.db import models

CODE_TYPE = [
    ('WASSCE', 'WASSCE'),
    ('BECE', 'BECE'),
    ('SHS PLACEMENT CODES', 'SHS PLACEMENT CODES')

]

class PinCode(models.Model):
    code_type = models.CharField(max_length=100, choices=CODE_TYPE)
    pin = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.code_type


class Payment(models.Model):
    code_type = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()
    reference = models.CharField(max_length=100, unique=True)
    is_successful = models.BooleanField(default=False)

    def __str__(self):
        return self.phone_number