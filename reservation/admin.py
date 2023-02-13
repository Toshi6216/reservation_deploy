from django.contrib import admin
from .models import Group, Event, Applying, Apploved

# Register your models here.
admin.site.register(Group)
admin.site.register(Event)
admin.site.register(Applying)
admin.site.register(Apploved)