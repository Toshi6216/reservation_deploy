from django.shortcuts import render, redirect
from django.views import View
from allauth.account import views  
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView
from django.urls import reverse_lazy, reverse
from reservation.models import *
from django.http import HttpResponse

from accounts.models import CustomUser
from .forms import ProfileForm
from django.http import HttpResponse,HttpResponseRedirect


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
    template_name = 'account/userprofile.html'

    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(email=self.request.user)
        group_data_m = ApprovedMember.objects.filter(member=user_data, approved=True)
        group_data_s = ApprovedStaff.objects.filter(staff=user_data, approved=True)
        # print(user_data.applyingmember_set.all())
        # applyings_m = user_data.applyingmember_set.all()
        # for applying_m in applyings_m:
        #     print(applying_m.group)
        join_event = Join.objects.filter(join_name=self.request.user, join=True).order_by('join_event__event_date')
        return render(request, self.template_name,{
            'group_data_m':group_data_m,
            'group_data_s':group_data_s,
            'user_data':user_data,
            'join_event':join_event,
        })

    def post(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(email=self.request.user)
        pk=user_data.pk
        if "applying_m_group" in request.POST:
            applying_member_pks = request.POST.getlist('applying_m_group')
            print(applying_member_pks)
            applying_member = ApplyingMember.objects.filter(pk__in=applying_member_pks, applying=True)
            print(applying_member)
            applying_member.delete()

        if "applying_s_group" in request.POST:
            applying_staff_pks = request.POST.getlist('applying_s_group')
            print(applying_staff_pks)
            applying_staff = ApplyingStaff.objects.filter(pk__in=applying_staff_pks, applying=True)
            print(applying_staff)
            applying_staff.delete()
            
        elif "event_join" in request.POST:
            join_pks = request.POST.getlist('event_join')
            join = Join.objects.filter(pk__in=join_pks, join=True)
            join.delete()
            
        return HttpResponseRedirect( reverse_lazy('userprofile', kwargs={'pk':pk}))
        

class ProfileEditView(OnlyYouMixin, UpdateView):
    model = CustomUser
    template_name = 'account/userprofile_form.html'
    form_class = ProfileForm
    
    def get_success_url(self):
        return reverse("userprofile", kwargs={"pk": self.kwargs["pk"]})

