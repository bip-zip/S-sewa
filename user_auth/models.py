from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

class User(AbstractUser):
    username = None
    phone = models.CharField(
        verbose_name='Phone Number',
        max_length=10,
        unique=True,
        null=True
    )
    email = models.EmailField(null=False, unique=True)
    document = models.FileField(null=False, upload_to ='userdocuments/')
    user_confirmed = models.BooleanField(default=False) #initially this field is false but will be change
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_admin = models.BooleanField(default=False)
    is_institution = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = [] #email and password are required fields and first name and last name is inherited from the user creation model

    #instanciate the usermanager object
    object = UserManager()

    def __str__(self):              # __unicode__ on Python 2
        return self.email


    @property
    def is_customer(self):
        "Is the user a member of customer?"
        return self.is_customer
    
    @property
    def is_institution(self):
        "Is the user a institution?"
        return self.is_institution
    
    @property
    def user_confirmed(self):
        "Is the user active?"
        return self.user_confirmed
    
    @property
    def username(self):
        name = self.email.split('@')[0]
        return name