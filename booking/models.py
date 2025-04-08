from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


def generate_unique_id():
    return str(uuid.uuid4())


class aTimeSlot(models.Model):
    id = models.CharField(
        primary_key=True, default=generate_unique_id, max_length=100)
    slot = models.CharField(max_length=10)
    room = models.IntegerField(null=True, blank=True)
    date = models.CharField(null=True, blank=True, max_length=10)
    name = models.CharField(null=True, blank=True, max_length=100)
    email = models.EmailField(null=True, blank=True)
    month = models.CharField(null=True, blank=True, max_length=2)
    year = models.CharField(null=True, blank=True, max_length=4)
    reason = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return str(self.slot)


class Booking(models.Model):
    FLOOR_CHOICES = [
        ('1st', '1st Floor'),
        ('2nd', '2nd Floor'),
        ('8th', '8th Floor'),
    ]
    
    time_slot = models.TimeField()
    booked_by = models.CharField(max_length=255)
    floor = models.CharField(max_length=10, choices=FLOOR_CHOICES)
    date = models.DateField()
    room = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['date', 'time_slot']
    
    def __str__(self):
        return f"{self.floor} Floor - {self.room} - {self.time_slot}"
