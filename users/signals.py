from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Customer

@receiver(pre_save, sender=Customer)
def set_customer_username(sender, instance, **kwargs):
    print(kwargs)