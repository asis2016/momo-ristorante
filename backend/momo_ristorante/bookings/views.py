"""
    bookings/views.py
    -----------------
"""
from django.views.generic import ListView, DetailView

from .models import Booking


class BookingListView(ListView):
    """ Booking List view. """
    model = Booking
    template_name = 'bookings/bookings.html'
    context_object_name = 'bookings'


class BookingDetailView(DetailView):
    """
    Booking detail view.
    """
    model = Booking
    template_name = 'bookings/detail.html'
    context_object_name = 'booking'
