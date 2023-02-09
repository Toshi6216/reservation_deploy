from django.urls import path
from reservation import views

urlpatterns = [
    path('',views.IndexView.as_view(), name="home"),
    path('event/',views.EventView.as_view(), name="event"),
    path('group/',views.GroupView.as_view(), name="group"),
]
