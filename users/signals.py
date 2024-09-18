from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Customer, Employee

"""
This file contains signals that are triggered when a customer or employee is deleted.
The signals are used to delete the user associated with the customer or employee.
""" # noqa


@receiver(post_delete, sender=Customer)
def delete_user_customer(sender, instance, **kwargs):
    """Delete user when customer is deleted."""
    instance.user.delete()


@receiver(post_delete, sender=Employee)
def delete_user_employee(sender, instance, **kwargs):
    """Delete user when employee is deleted."""
    instance.user.delete()
