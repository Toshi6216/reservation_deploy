from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Event_cal
from .forms import EventForm
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
import time
import json
from django.middleware.csrf import get_token

def calendarView(request):
    """
    カレンダー画面
    """
   # get_token(request)
    template = loader.get_template("full_calendar/calendar.html")
    return HttpResponse(template.render())

def add_event(request):
    """
    イベント登録
    """
    if request.method == "GET":
        #GETは対応しない
        raise Http404()

    #JSONの解析
    datas = json.loads(request.body)

    #バリデーション
    eventForm = EventForm(datas)
    if eventForm.is_valid() == False:
        #バリデーションエラー
        raise Http404

    #リクエストの取得
    event_title = datas["event_title"]
    event_detail = datas["event_detail"]

    
    #登録処理
    event = Event_cal(
        event_title = str(event_title),
        event_detail = str(event_detail),
       
    )
    event.save()

    #空を返却
    return HttpResponse("")