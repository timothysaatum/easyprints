# Generated by Django 5.0.7 on 2024-07-24 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_payment_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='pincode',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
