from django.shortcuts import render, redirect

from django.contrib import messages
from attendify.forms import AttendeeForm
from attendify.models import Attendee
from .mpesa import initiate_stk_push

def register_attendee(request):
    if request.method =='POST':
        if form.is_valid():
            attendee = form.save()

            payment_response = initiate_stk_push(attendee.phone_number, 10)
            if payment_response['status'] == 'success':
                attendee.payment_status = True
                attendee.payment_reference = payment_response['reference']
                attendee.save()
                messages.success(request, "Registration successful! Payment recieved.")
                return redirect('success_page')
            else:
                messages.error(request, "Payment failed. Please try again.")
    else:
        form = AttendeeForm()
    return render(request, 'attendify/register.html', {'form': form})



def landing_page(request):
    return render(request, 'attendify/landing.html')