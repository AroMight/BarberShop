from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class TagsNames(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class TaggedItem(models.Model):
    name = models.ForeignKey(TagsNames, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.name