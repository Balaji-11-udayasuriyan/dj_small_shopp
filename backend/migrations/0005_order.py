# Generated by Django 5.1.5 on 2025-01-30 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('order_number', models.CharField(blank=True, max_length=255, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('order_status', models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], default='PENDING', max_length=255)),
                ('payment_method', models.CharField(choices=[('CASH', 'CASH'), ('UPI', 'UPI'), ('CARD', 'CARD')], default='CASH', max_length=255)),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
