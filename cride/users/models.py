"""User model"""


#Django
from django.db import models
from django.contrib.auth.models import AbstractUser


#utilities
from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """Usermodel.


        Extend  from Django's Abstract User, change the username field
        to email and add some filed
    
    
    """
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique':'A user with that email already exists'
        }
    )

    phone_number = models.CharField(max_length=17, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firts_name', 'last_name']

    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'Help easily distinguish users and perform quieries.'
            'Clients are the main type of user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified its email address'

    )
