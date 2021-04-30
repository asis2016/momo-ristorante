"""
    bookings/models.py
    ------------------
    In booking, any guest can reserve a table.
    He / She can post a note also.
    Optional: New booking is notified to the manager via email.
    Only employees (all as of v.1.0) can view booking information.
"""
from django.db import models


class Booking(models.Model):
    """ Booking model as of v.1.0 """
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.TextField()
    person = models.IntegerField()
    note = models.TextField(blank=True)
    create_date = models.DateField()
    status = models.BooleanField(default=0)
    modify_date = models.DateField()

    def __str__(self):
        return str(self.fullname)
