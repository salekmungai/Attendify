from django import forms
from attendify.models import Attendee

class AttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['name', 'phone_number']
