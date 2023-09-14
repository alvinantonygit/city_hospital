from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    jls_extract_var = 'date'
    input_type =jls_extract_var


class BookingForm(forms.ModelForm):
        class Meta:
            model = Booking
            fields='__all__'

            widgets ={
                'booking_date':DateInput(),
            }

            labels ={
                'p_name':"Patient Name:",
                'p_phone':"Patient Phone:",
                'p_email':"Email:",
                'doc_name':"Doctor Name:",
                'booking_date':"Booking Date:",

            }
