"""User model"""


#Django
from django.db import models
from django.contrib.auth.models import AbstractUser


#utilities
from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """Usermodel.

    
    
    """
    pass
