# Generated by Django 5.0.7 on 2024-07-23 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_pincode_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='code_type',
            field=models.CharField(default='WASSCE', max_length=50),
            preserve_default=False,
        ),
    ]
