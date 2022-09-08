from django.contrib import admin
from .models import Youtuber
# Register your models here.

class YtAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subs_count', 'is_featured')
    search_fields = ('name', 'camera_type', 'city')
    list_filter = ('camera_type', 'category')
    list_display_links = ('id', 'name')
    list_editable = ('is_featured',)


admin.site.register(Youtuber, YtAdmin)