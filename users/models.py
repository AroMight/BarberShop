from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError


class Branch(models.Model):
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to='users/covers/branches/%Y/%m/%d', null=True, blank=True, default='')

    def __str__(self):
        return str(self.district)


class BaseUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(
        max_length=15, blank=True, null=True)
    profile_photo = models.ImageField(
        upload_to='users/covers/users/%Y/%m/%d', null=True, blank=True, default='')

    class Meta:
        abstract = True


class Customer(BaseUser):
    pass

    def __str__(self):
        return str(self.user)
    
    def clean(self):
        if self.phone_number:
            if Customer.objects.filter(phone_number=self.phone_number).exclude(pk=self.pk).exists():
                raise ValidationError(
                    {'phone_number': 'This number is already in use.'})


class Employee(BaseUser):
    work_at = models.ForeignKey(Branch, on_delete=models.CASCADE)
    services_done = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)
