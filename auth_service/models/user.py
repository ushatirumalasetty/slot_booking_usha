from django.contrib.auth.models import AbstractUser
from django.db import models
from slot_booking.constants.enums import *

class User(AbstractUser):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    user_name = models.CharField(max_length=50, null=False)
    role=models.CharField(max_length=50, choices=UserRole.get_list_of_tuples(),
                         default="USER")
