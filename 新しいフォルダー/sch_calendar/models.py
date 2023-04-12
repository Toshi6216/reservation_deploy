from django.db import models
import datetime
from django.utils import timezone

class Schedule(models.Model):
    """スケジュール"""
    sammary = models.CharField("概要", max_length=50)
    descripthin = models.TextField("詳細", blank=True)
    start_time = models.TimeField("開始時間" )
    end_time = models.TimeField("終了時間")
    date = models.DateField("日付")
    created_at = models.DateTimeField("作成日", default=timezone.now)
    

    def __str__(self):
        return self.sammary
