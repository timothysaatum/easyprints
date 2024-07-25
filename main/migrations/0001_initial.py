# Generated by Django 5.0.7 on 2024-07-25 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('reference', models.CharField(max_length=100, unique=True)),
                ('is_successful', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PinCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_type', models.CharField(choices=[('WASSCE', 'WASSCE'), ('BECE', 'BECE'), ('SHS PLACEMENT CODES', 'SHS PLACEMENT CODES')], max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pin', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('is_used', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
