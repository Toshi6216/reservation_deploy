from django import forms
from .models import *

class EventForm(forms.ModelForm):
    class Meta:
        model = Event_cal
        fields = (
            "event_title", 
            "event_detail",
    
            )

        