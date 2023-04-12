from django.db import models


class Event_cal(models.Model):
    event_title = models.CharField(max_length=150)
    event_detail = models.TextField()

    # event_date = models.DateField()
    # start_time = models.TimeField()
    # end_time = models.TimeField()

    def __str__(self):
        return self.event_title
