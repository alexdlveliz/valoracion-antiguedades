""" Titrations model """

# Django
from django.db import models

# Utilities
from valoracion.utils.models import ParentModel


class Titration(ParentModel):
    """ Titration model
    A titration is some kind of score that is given
    to a product by the titrators
    """

    profile = models.ForeignKey('users.profile', related_name='profile', on_delete=models.CASCADE)

    product = models.ForeignKey('products.product', related_name='product', on_delete=models.CASCADE)

    score = models.FloatField(
        default=3.0,
        help_text='The score of a product, given by a titrator, going from 1 to 5'
    )

    reference = models.TextField(max_length=500, null=True)

    def __str__(self):
        """ returns the titration reference """
        return str(self.score)