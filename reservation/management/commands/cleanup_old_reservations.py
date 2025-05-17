from django.core.management.base import BaseCommand
from django.utils import timezone
from reservation.models import Event
from datetime import timedelta
import csv
import os

class Command(BaseCommand):
    help = 'Backup Events older than 90 days (no delete)'

    def handle(self, *args, **kwargs):
        threshold_date = timezone.now() - timedelta(days=90)
        old_events = Event.objects.filter(event_date__lt=threshold_date)

        if not old_events.exists():
            self.stdout.write("🟡 古いイベントは見つかりませんでした。")
            return

        # バックアップディレクトリ作成
        backup_dir = 'backups'
        os.makedirs(backup_dir, exist_ok=True)

        timestamp = timezone.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(backup_dir, f'event_backup_{timestamp}.csv')

        with open(backup_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            # ヘッダー：イベントの全フィールド名
            event_fields = [f.name for f in Event._meta.fields]
            writer.writerow(event_fields)

            # 各データ行を書き込み
            for event in old_events:
                row = [getattr(event, f) for f in event_fields]
                writer.writerow(row)

        self.stdout.write(f"✅ バックアップ完了：{backup_file}")
        self.stdout.write("⚠️ データ削除は行っていません。安心して確認してください。")
