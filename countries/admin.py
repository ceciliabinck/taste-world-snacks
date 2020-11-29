from django.contrib import admin
from .models import Country

# Register your models here, that will appear in the database admin.


class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'about',
        'image',
    )


admin.site.register(Country, CountryAdmin)
