import os
from django.db.models.signals import pre_delete, post_delete, pre_save
from django.dispatch import receiver
from .models import Customer, Employee

"""
This file contains signals that are triggered when a customer or employee is deleted.
The signals are used to delete the user associated with the customer or employee.
"""  # noqa


def delete_user(instance):
    """Delete the associated user when the related object is deleted."""
    if instance.user:
        instance.user.delete()


def delete_old_cover_image(instance):
    """Delete the old cover image when a new one is uploaded."""
    try:
        os.remove(instance.profile_photo.path)
    except (FileNotFoundError, ValueError) as e:
        print(e)


@receiver(post_delete, sender=Customer)
@receiver(post_delete, sender=Employee)
def delete_user_on_related_model_delete(sender, instance, *args, **kwargs):
    delete_user(instance)


@receiver([pre_delete, pre_save], sender=Employee)
def delete_old_cover_image_on_employee_delete(sender, instance, *args, **kwargs):
    old_instance = Employee.objects.filter(pk=instance.pk).first()

    if old_instance is not None:
        is_new_cover = old_instance.profile_photo != instance.profile_photo

        if is_new_cover:
            delete_old_cover_image(old_instance)
        else:
            pass
