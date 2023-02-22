from django.shortcuts import render
from django.views.generic import TemplateView, View, UpdateView
from .models import Group, Event, Approved, Applying
from .forms import EventForm, GroupForm
from accounts.models import CustomUser
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
import time
import json
from django.middleware.csrf import get_token
from django.views import generic
from . import mixins

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

class EventEditView(UpdateView):
    model = Event
    template_name = 'reservation/event_form.html'
    form_class = EventForm
    success_url = reverse_lazy('event')

    def get(self, request, **kwargs):
        event_data = Event.objects.get(id=self.kwargs['pk'])
        approved_data = Approved.objects.filter(
            group = event_data.group)

        names = [data.approved_user for data in approved_data] 
        #スタッフユーザーで無ければHTMLを返す　遷移させる
        if not request.user.is_staff:
            return HttpResponse('<h1>%sさんはアクセスできませぬ</h1>' % request.user.nickname)
        elif not request.user in names:
            return HttpResponse('<h1>%sさんは%sのMemberではありませぬ</h1>' % (request.user.nickname, event_data.group ))
        return super().get(request)

class GroupEditView(UpdateView):
    model = Group
    template_name = 'reservation/group_form.html'
    form_class = GroupForm
    success_url = reverse_lazy('group')

    def get(self, request, **kwargs):
        group_data = Group.objects.get(id=self.kwargs['pk'])
        approved_data = Approved.objects.filter(
            group = group_data)

        names = [data.approved_user for data in approved_data] 
        #スタッフユーザーで無ければHTMLを返す　遷移させる
        if not request.user.is_staff:
            return HttpResponse('<h1>%sさんはアクセスできませぬ</h1>' % request.user.nickname)
        elif not request.user in names:
            return HttpResponse('<h1>%sさんは%sのMemberではありませぬ</h1>' % (request.user.nickname, group_data.group_name ))
        return super().get(request)

class GroupDetailView(View):
    def get(self, request, *args, **kwargs):
        group_data = Group.objects.get(id=self.kwargs['pk'])
        approved_data = Approved.objects.filter(
            group = group_data)

        names = [data.approved_user for data in approved_data] 
        """グループ加入の承認済みデータのリストに名前が入っていないと別ページにリダイレクトされる"""
        # print(f"approved_data: {approved_data}")
        # print(type(approved_data))
        # print(f"names:{names}")
        # print(f"request.user:{request.user}")
        # print(request.user in names)
        if not request.user in names:
            return HttpResponse('<h1>%sさんは%sのMemberではありませぬ</h1>' % (request.user.nickname, group_data.group_name ))

        return render(request, 'reservation/group_detail.html',{
            'group_data':group_data,
            'approved_data':approved_data,
        })



class EventCalView(mixins.MonthCalendarMixin, generic.TemplateView):
    template_name = 'reservation/event_cal.html'
    model = Event
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        event_data = Event.objects.order_by('-id') #イベントのデータを読み出し
        context.update(calendar_context)
        context['event_data'] = event_data #イベントのデータをコンテキストで渡す
        
        return context

class GpEventCalView(mixins.MonthCalendarMixin, generic.TemplateView):
    template_name = 'reservation/group_event_cal.html'
    model = Event
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        try:
            approved = Approved.objects.get(approved_user=self.request.user)
            event_data = Event.objects.filter(group=approved.group).order_by('-id') #イベントのデータを読み出し
        except:
            event_data = []
        context.update(calendar_context)
        context['event_data'] = event_data #イベントのデータをコンテキストで渡す
        
        return context