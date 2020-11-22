""" Products admin """

# Django
from django.contrib import admin

# Models
from valoracion.products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Product admin """

    list_display = (
        'name',
        'description'
    )

    search_fields = ('name', 'description')