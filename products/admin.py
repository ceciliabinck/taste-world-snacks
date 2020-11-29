from django.contrib import admin
from .models import Product, Category

# Register your models here, that will appear in the database admin.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'country',
        'category',
        'price',
        'image'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
