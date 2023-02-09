from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import Group, Event

class IndexView(TemplateView):
    template_name = 'reservation/index.html'

class EventView(View):
    #このviewがコールされたら最初にget関数が呼ばれる
    def get(self, request, *args, **kwargs):
        event_data = Event.objects.order_by('-id') #新しいものから順番に並べる
        return render(request, 'reservation/event_index.html',{
            'event_data': event_data
        })

class GroupView(View):
    #このviewがコールされたら最初にget関数が呼ばれる
    def get(self, request, *args, **kwargs):
        group_data = Group.objects.order_by('-id') #新しいものから順番に並べる
        return render(request, 'reservation/group_index.html',{
            'group_data': group_data
        })