# Generated by Django 5.1 on 2024-09-11 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_customer_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='services_done',
        ),
    ]
