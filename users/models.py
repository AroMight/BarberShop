import os
from PIL import Image
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Branch(models.Model):
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to="users/covers/branches/%Y/%m/%d", null=True, blank=True, default=""
    )

    def __str__(self):
        return str(self.district)


class BaseUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        abstract = True


class Customer(BaseUser):
    pass

    def __str__(self):
        return str(self.user)


class Employee(BaseUser):
    work_at = models.ForeignKey(Branch, on_delete=models.CASCADE)
    profile_photo = models.ImageField(
        upload_to="users/covers/users/%Y/%m/%d", null=True, blank=True, default=""
    )

    def __str__(self):
        return str(self.user)

    @staticmethod
    def resize_image(image, new_width=300):
        """Resize an image to a new width."""
        image_full_path = os.path.join(settings.MEDIA_ROOT, image.name)
        print(image_full_path)
        image_pillow = Image.open(image_full_path)
        original_width, original_height = image_pillow.size

        if original_width <= new_width:
            image_pillow.close()
            return

        new_height = round((new_width / original_width) * original_height)

        new_image_pillow = image_pillow.resize((new_width, new_height), Image.LANCZOS)
        new_image_pillow.save(
            image_full_path,
            optimize=True,
            quality=30,
        )

    def save(self, *args, **kwargs):
        saved = super().save(*args, **kwargs)
        if self.profile_photo:
            try:
                self.resize_image(self.profile_photo)
            except FileNotFoundError:
                pass
        return saved
