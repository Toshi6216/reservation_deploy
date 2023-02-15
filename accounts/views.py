from django.shortcuts import render, redirect
from django.views import View
from allauth.account import views  
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView
from django.urls import reverse_lazy, reverse

from accounts.models import CustomUser
from .forms import ProfileForm

#user確認用view
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのユーザー情報ページのpkが同じか、又はスーパーユーザーなら許可
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

#Profile内容確認用view
class ProfileView(OnlyYouMixin, DetailView):
    model = CustomUser
    template_name = 'account/profile.html'

class ProfileEditView(OnlyYouMixin, UpdateView):
    model = CustomUser
    template_name = 'account/profile_form.html'
    form_class = ProfileForm
    
    def get_success_url(self):
        return reverse("profile", kwargs={"pk": self.kwargs["pk"]})

