from django.db import models
from accounts.models import CustomUser, StaffUser, MemberUser


class Group(models.Model):
    group_name = models.CharField(max_length=150)
    group_detail = models.TextField()
    group_owner = models.ForeignKey(
        StaffUser,
        unique=False,
        db_index=True,
        related_name='staff_user',
        on_delete=models.CASCADE
    )
 
    def __str__(self):
        return self.group_name
    
class Event(models.Model):
    event_title = models.CharField(max_length=150)
    event_detail = models.TextField()
    group = models.ForeignKey(Group,  on_delete=models.CASCADE)
    event_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.event_title

#グループへ加入承認済(member)
class ApprovedMember(models.Model):
    member = models.ForeignKey(CustomUser,  on_delete=models.CASCADE)
    group = models.ForeignKey(Group,  on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["member", "group"],
                name = "approved_member_unique"
            ),
        ]

#グループへ加入承認済(staff)
class ApprovedStaff(models.Model):
    staff = models.ForeignKey(CustomUser,  on_delete=models.CASCADE)
    group = models.ForeignKey(Group,  on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["staff", "group"],
                name = "approved_staff_unique",
            ),
        ]

#加入申請中(member)
class ApplyingMember(models.Model):
    member = models.ForeignKey(CustomUser, on_delete=models.CASCADE, )
    group = models.ForeignKey(Group, on_delete=models.CASCADE,)
    applying = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["member", "group"],
                name = "appliyng_member_unique"
            ),
        ]

#加入申請中(staff)
class ApplyingStaff(models.Model):
    staff = models.ForeignKey(CustomUser, on_delete=models.CASCADE, )
    group = models.ForeignKey(Group, on_delete=models.CASCADE,
    )
    applying = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["staff", "group"],
                name = "appliyng_staff_unique"
            ),
        ]


class Join(models.Model):
    join_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    join_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    join = models.BooleanField(default=False)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["join_name","join_event"],
                name = "join_unique"
            ),
        ]