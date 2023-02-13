from django.db import models
from accounts.models import CustomUser


class Group(models.Model):
    group_name = models.CharField(max_length=150)
    group_detail = models.TextField()
 

    def __str__(self):
        return self.group_name

class Event(models.Model):
    event_title = models.CharField(max_length=150)
    event_detail = models.TextField()

    def __str__(self):
        return self.event_title

class Apploved(models.Model):
    applouved_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    applouved = models.BooleanField(default=False)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["applouved_user", "group"],
                name = "applouved_unique"
            ),
        ]
    
class Applying(models.Model):
    applying_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name = "applying_user")
    applying_group = models.ForeignKey(Group, on_delete=models.CASCADE,
    related_name = "applying_group")
    applying = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["applying_user", "applying_group"],
                name = "appliyng_unique"
            ),
        ]