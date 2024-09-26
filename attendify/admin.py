from django.contrib import admin
from .models import Attendee

@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'payment_status')
    search_fields = ['name',]
    
