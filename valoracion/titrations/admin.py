""" Titrations admin """

# Django
from django.contrib import admin

# Models
from valoracion.titrations.models import Titration


@admin.register(Titration)
class TitrationAdmin(admin.ModelAdmin):
    """ Titration admin """

    list_display = (
        'profile',
        'product',
        'score'
    )

    search_fields = ('profile', 'product')

    list_filter = ('profile', 'product')