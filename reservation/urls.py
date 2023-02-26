from django.urls import path
from reservation import views


urlpatterns = [
    path('',views.IndexView.as_view(), name="home"),
    path('event/',views.EventView.as_view(), name="event"),
    path('group/',views.GroupView.as_view(), name="group"),
    path('event_edit/<int:pk>/',views.EventEditView.as_view(), name="event_edit"),
    path('group_edit/<int:pk>/',views.GroupEditView.as_view(), name="group_edit"),
    path('group_detail/<int:pk>/',views.GroupDetailView.as_view(), name="group_detail"),
    path('event_cal/',views.EventCalView.as_view(), name="event_cal"),
    path('event_cal/<int:year>/<int:month>/',views.EventCalView.as_view(), name="event_cal"),
    path('gp_event_cal/<int:year>/<int:month>/',views.GpEventCalView.as_view(), name="gp_event_cal"),
    path('gp_event_cal/',views.GpEventCalView.as_view(), name="gp_event_cal"),
    path('event/new/', views.EventCreateView.as_view(), name='event_new'),
    path('group/new/', views.GroupCreateView.as_view(), name='group_new'),


]
