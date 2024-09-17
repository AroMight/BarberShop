from django.contrib import admin
from .models import TaggedItem, TagName


class TagNameAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 20


class TaggedItemAdmin(admin.ModelAdmin):
    list_display = ['tag', 'content_type', 'object_id']
    list_filter = ['tag', 'content_type']
    search_fields = ['tag']
    list_per_page = 20
    


admin.site.register(TaggedItem, TaggedItemAdmin)
admin.site.register(TagName, TagNameAdmin)
