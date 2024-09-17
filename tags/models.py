from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class TaggedItem(models.Model):
    tag = models.CharField(max_length=100)

    # This is the foreign key to the content type
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    # This is the object id
    object_id = models.PositiveIntegerField()

    # This is the actual object (default to 'content_type' and 'object_id')
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.tag