# Generated by Django 5.1 on 2024-08-19 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_customer_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_photo',
        ),
    ]
