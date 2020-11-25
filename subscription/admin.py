from django.contrib import admin
from .models import Box, Length

# Register your models here.


class BoxAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'price',
        'image_url',
    )


class LengthAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'length',
    )


admin.site.register(Box, BoxAdmin)
admin.site.register(Length, LengthAdmin)
