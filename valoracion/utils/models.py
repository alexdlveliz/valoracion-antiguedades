""" Django models utilities """

# Django
from django.db import models

class ParentModel(models.Model):
    """ Valoración base model
    
    This parent model acts as an abstract base class from which every
    other model will inherit.
    This model provides every other model with the following:
        - created (DateTime): when the object was created
        - modified (DateTime): when the object was modified
    """
    
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was modified'
    )

    class Meta:
        """ Meta options """
        abstract = True
        get_latest_by = 'created',
        ordering = ['-created', '-modified']