from django.urls import path
from accounts import views

urlpatterns = [
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('profile_form/<int:pk>/', views.ProfileEditView.as_view(), name='profile_form'),

]