from django import forms
from .models import *

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        # fields = (
        #     "event_title", 
        #     "event_detail",
    
        #     )

        
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ("group_name", "group_detail")