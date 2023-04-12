from django.urls import path
from full_calendar import views

urlpatterns = [
    
    path('fullcalendar/',views.calendarView, name="fullcalendar"),
    path('event_add/', views.add_event, name="add_event"),
]
