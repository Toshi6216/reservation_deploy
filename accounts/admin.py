from django.contrib import admin
from .models import CustomUser, StaffUser, MemberUser

admin.site.register(CustomUser)
admin.site.register(StaffUser)
admin.site.register(MemberUser)