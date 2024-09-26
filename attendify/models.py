from django.db import models

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    payment_status = models.BooleanField(default=False)
    payment_reference = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name