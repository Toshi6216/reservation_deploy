from django.db import models
#from accounts.models import CustomUser


class Group(models.Model):
    group_name = models.CharField(max_length=150)
    group_detail = models.TextField()
    #staff = 

    def __str__(self):
        return self.group_name

class Event(models.Model):
    event_title = models.CharField(max_length=150)
    event_detail = models.TextField()

    def __str__(self):
        return self.event_title

