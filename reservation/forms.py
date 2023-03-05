from django import forms
from .models import *
from datetime import time

class EventForm(forms.ModelForm):
    
    class Meta:
        model = Event
        # fields = '__all__'
        fields = (
            "event_title", 
            "event_detail",
            "event_date",
            "start_time",
            "end_time",
    
            )
        widgets = { 
            # "event_date":forms.SelectDateWidget,#プルダウンで日付入力
            'start_time':forms.TimeInput(format='%H:%M'),
            'end_time':forms.TimeInput(format='%H:%M'),
        }

   

        
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ("group_name", "group_detail")