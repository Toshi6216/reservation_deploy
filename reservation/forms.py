from django import forms
from .models import *
from datetime import time
from django.forms import widgets

class EventForm(forms.ModelForm):
    # -------案１------
    # start_time = forms.TimeField(widget=forms.Select(choices=[(time(hour=x, minute=y), '{:02d}:00'.format(x)) for x in range(0, 24)]))
    # end_time = forms.TimeField(widget=forms.Select(choices=[(time(hour=x, minute=0), '{:02d}:00'.format(x)) for x in range(0, 24)]))
    # ---------------------

    # -------案2------
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['start_time'] = forms.TimeField(widget=forms.Select(choices=self.time_choices()))
    #     self.fields['end_time'] = forms.TimeField(widget=forms.Select(choices=self.time_choices()))

    # def time_choices(self):
    #     choices = []
    #     hours = range(0, 24)
    #     minutes = range(0, 60, 10)  # 10分刻みにする
    #     for hour in hours:
    #         for minute in minutes:
    #             time_obj = time(hour=hour, minute=minute)
    #             formatted_time = time_obj.strftime('%H:%M')
    #             choices.append((time_obj, formatted_time))
    #     return choices
    # ---------------------
    start_time = forms.TimeField(input_formats=['%H:%M'])
    end_time = forms.TimeField(input_formats=['%H:%M'])

    start_hour = forms.ChoiceField(choices=[(str(x), '{:02d}'.format(x)) for x in range(0, 24)])
    start_minute = forms.ChoiceField(choices=[(str(x), '{:02d}'.format(x)) for x in range(0, 60)])
    end_hour = forms.ChoiceField(choices=[(str(x), '{:02d}'.format(x)) for x in range(0, 24)])
    end_minute = forms.ChoiceField(choices=[(str(x), '{:02d}'.format(x)) for x in range(0, 60)])

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
        widgets = { 
            # "event_date":forms.SelectDateWidget,#プルダウンで日付入力
            'start_time':forms.TimeInput(format='%H:%M'),
            'end_time':forms.TimeInput(format='%H:%M'),
        }

   

        
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ("group_name", "group_detail")