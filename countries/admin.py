from django.contrib import admin
from .models import Country

# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'about',
        'image',
    )


admin.site.register(Country, CountryAdmin)
