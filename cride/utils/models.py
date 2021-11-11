"""Django models utilities"""

#Django
from django.db import models

class CRideModel(models.Model):
    """comparte Ride base model
    
        CRideModel acts as an abstract base class from which every
        other model in the project will inherit. this class provides
        every table with the following attributes:
                + created (DateTime): Store the datetime the object was created
                + modified (DateTime): Store the last datetime the object was modified

    """
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the was created'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the was last modified'
    )

    class Meta:
        asbtract = True
        get_lastest_by = 'created'
        ordering= ['-created', '-modified']
