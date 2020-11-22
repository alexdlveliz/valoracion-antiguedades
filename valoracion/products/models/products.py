""" Products model """

# Django
from django.db import models

# Utilities
from valoracion.utils.models import ParentModel

class Product(ParentModel):
    """ Product model

    A product is an antiquity on sale in the store, it 
    has a name and a description, and titrations made by the users
    """

    name = models.CharField('Product name', max_length=140)
    
    description = models.TextField(max_length=500)

    is_sold = models.BooleanField(default=False)

    def __str__(self):
        """ returns product's str representation """
        return self.name