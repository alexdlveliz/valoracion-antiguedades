""" Titrations admin """

# Django
from django.contrib import admin

# Models
from valoracion.titrations.models import Titration


@admin.register(Titration)
class TitrationAdmin(admin.ModelAdmin):
    """ Titration admin """

    list_display = (
        'user',
        'product',
        'score'
    )

    search_fields = ('user', 'product')

    list_filter = ('user', 'product', 'score')