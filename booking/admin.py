from django.contrib import admin
from .models import aTimeSlot, Booking
# Register your models here.


class SHAdmin(admin.ModelAdmin):
    list_display = ['slot', 'name', 'date']
    
class BookingAdmin(admin.ModelAdmin):
    list_display = ['floor', 'room', 'time_slot', 'booked_by', 'date']
    list_filter = ['floor', 'date']
    search_fields = ['booked_by', 'room']

admin.site.register(aTimeSlot, SHAdmin)
admin.site.register(Booking, BookingAdmin)
