from django.contrib import admin
from .models import TaggedItem, TagsNames


@admin.register(TagsNames)
class TagsNamesAdmin(admin.ModelAdmin):
    pass


@admin.register(TaggedItem)
class TagsNamesAdmin(admin.ModelAdmin):
    list_display = [
        "tag",
        "content_type",
        "object_id",
        "content_object",
    ]
