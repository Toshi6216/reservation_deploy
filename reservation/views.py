from django.shortcuts import render
from django.views.generic import TemplateView, View, UpdateView
from .models import Group, Event, Apploved, Applying
from .forms import EventForm, GroupForm
from accounts.models import CustomUser
from django.urls import reverse_lazy
from django.http import HttpResponse

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
        #スタッフユーザーで無ければHTMLを返す　遷移させる
        if not request.user.is_staff:
            return HttpResponse('<h1>%sさんはアクセスできませぬ</h1>' % request.user.nickname)
        return super().get(request)

class GroupEditView(UpdateView):
    model = Group
    template_name = 'reservation/group_form.html'
    form_class = GroupForm
    success_url = reverse_lazy('group')

    def get(self, request, **kwargs):
        #スタッフユーザーで無ければHTMLを返す　遷移させる
        if not request.user.is_staff:
            return HttpResponse('<h1>%sさんはアクセスできませぬ</h1>' % request.user.nickname)
        return super().get(request)

class GroupDetailView(View):
    def get(self, request, *args, **kwargs):
        group_data = Group.objects.get(id=self.kwargs['pk'])
        applying_data = Applying.objects.filter(
            applying_group = group_data)

        name = [data.applying_user for data in applying_data]
        print(applying_data)
        print(type(applying_data))
        print(name)
        print(request.user in name)
        if not request.user in name:
            return HttpResponse('<h1>%sさんはMemberではありませぬ</h1>' % request.user.nickname, )
        

        return render(request, 'reservation/group_detail.html',{
            'group_data':group_data,
            'applying_data':applying_data
        })