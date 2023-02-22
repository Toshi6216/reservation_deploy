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
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    event_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.event_title

#グループへ加入承認済
class Approved(models.Model):
    approved_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["approved_user", "group"],
                name = "approved_unique"
            ),
        ]

#加入申請中
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