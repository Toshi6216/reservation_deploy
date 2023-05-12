from django import forms
from .models import *
from datetime import time
from django.forms import widgets
import datetime

class EventForm(forms.ModelForm):

    start_time = forms.TimeField(label="開始時刻",widget=forms.TimeInput(attrs={'type': 'time'}))
    end_time = forms.TimeField(label="終了時刻", widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Event
        # fields = '__all__'
        fields = [
            "event_title", 
            "event_detail",
            "event_date",
            "start_time",
            "end_time",
    
        ]
        labels={
            "event_title":"タイトル", 
            "event_detail":"内容",
            "event_date":"開催日",
        }

class SearchForm(forms.Form):
    keyword = forms.CharField(
        label='', 
        max_length=50, 
        required=False,
        )



   

        
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ("group_name", "group_detail")