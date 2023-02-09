from django.urls import path
from accounts import views

urlpatterns = [
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
#    path('login/', views.LoginView.as_view(), name='login'),

]