""" Profiles model """

# Django
from django.db import models

# Utilities
from valoracion.utils.models import ParentModel


class Profile(ParentModel):
    """ Profile model
    The profile holds the users's public data, as well as
    the user's state, if it's a titrator or not.
    """

    user = models.OneToOneField('users.user', on_delete=models.CASCADE)

    biography = models.TextField(max_length=500, blank=True)

    # State
    is_titrator = models.BooleanField(
        'Titrator',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries accordingly '
            'Titrators are the main type of user'
        )
    )

    def __str__(self):
        """ Return users' str representations """
        return str(self.user)
