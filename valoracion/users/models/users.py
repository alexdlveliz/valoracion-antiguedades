""" User model """

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from valoracion.utils.models import ParentModel

class User(ParentModel, AbstractUser):
    """ User model
    Extends from Django's Abstract User and the parent model
    Change the username field to email and add extra fields
    """
    
    email = models.EmailField(
        'Email address',
        unique=True,
        error_messages={
            'unique': 'This email is already being used'
        }
    )

    phone_regex = RegexValidator(
        regex = r'\+?1?\d{9,15}$',
        message = 'Phone must be entered in the following format: +999999999. Up to 15 digits'
    )

    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    # Field declaration to bypass the username field with the email
    USERNAME_FIELD = 'email'

    # Field declaration to bypass the required fields
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_titrator = models.BooleanField(
        'Titrator',
        default=True,
        help_text = (
            'Help easily distinguish users and perform queries accordingly'
            'Titrators are the main type of user'
        )
    )

    def __str__(self):
        """ return username """
        return self.username
    
    def get_short_name(self):
        """ return username """
        return self.username