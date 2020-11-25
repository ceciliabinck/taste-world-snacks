from django.contrib import admin
from .models import Box

# Register your models here.


class BoxAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image'
        'price',
        'image_url',
    )


admin.site.register(Box, BoxAdmin)
