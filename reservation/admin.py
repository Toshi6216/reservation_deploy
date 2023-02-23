from django.contrib import admin
from .models import *

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'group', 'event_date', 'start_time', 'end_time')

class ApplyingMemberAdmin(admin.ModelAdmin):
    list_display = ('member', 'group', 'applying')

class ApplyingStaffAdmin(admin.ModelAdmin):
    list_display = ('staff', 'group', 'applying')

class ApprovedMemberAdmin(admin.ModelAdmin):
    list_display = ('member', 'group', 'approved')

class ApprovedStaffAdmin(admin.ModelAdmin):
    list_display = ('staff', 'group', 'approved',)

admin.site.register(Group)
admin.site.register(Event, EventAdmin)
admin.site.register(ApplyingMember, ApplyingMemberAdmin)
admin.site.register(ApplyingStaff, ApplyingStaffAdmin)
admin.site.register(ApprovedMember, ApprovedMemberAdmin)
admin.site.register(ApprovedStaff, ApprovedStaffAdmin)
