from django.contrib.auth.models import AbstractUser
from django.db import models
from slot_booking.constants.enums import *

class User (AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, null=False)

class WashingMachine(models.Model):
    washing_machine_id = models.CharField(max_length=50)
    status= models.CharField(
      max_length=10,
      choices=[(washing_machine_status.name,washing_machine_status.value)
               for washing_machine_status in WashingMachineStatus],
               default = "ACTIVE"
    )

class WashingMachineSlot(models.Model):
    washing_machine = models.ForeignKey(WashingMachine,
                             on_delete=models.CASCADE,
                             related_name='washing_machine_bookings')
    start_time = models.TimeField()
    end_time = models.TimeField()
    day= models.CharField(
      max_length=10,
      choices=[(day.name,day.value) for day in Days]
    )


class UserSlot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='user_bookings')
    washing_machine= models.ForeignKey(WashingMachineSlot, on_delete=models.CASCADE,
                             related_name='slot_bookings')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

class DaysRange(models.Model):
    days_range = models.IntegerField()


class Request(models.Model):
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    requested_user_slot = models.ForeignKey(UserSlot, on_delete=models.CASCADE)
    request_status= models.CharField(
      max_length=10,
      choices=[(request_status.name,request_status.value)
               for request_status in RequestStatus],
               default = "PENDING"
    )
