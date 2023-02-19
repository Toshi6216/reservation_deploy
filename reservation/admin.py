from django.contrib import admin
from .models import Group, Event, Applying, Approved

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'group')

class ApplyingAdmin(admin.ModelAdmin):
    list_display = ('applying_user', 'applying_group', 'applying')

class ApprovedAdmin(admin.ModelAdmin):
    list_display = ('approved_user', 'group', 'approved')

admin.site.register(Group)
admin.site.register(Event, EventAdmin)
admin.site.register(Applying, ApplyingAdmin)
admin.site.register(Approved, ApprovedAdmin)