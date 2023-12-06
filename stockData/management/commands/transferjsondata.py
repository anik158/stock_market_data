
from django.core.management.base import BaseCommand
from stockData.models import JsonStockData, SqlStockData

class Command(BaseCommand):
    help = 'Migrate data from JSON model to SQL model'

    def handle(self, *args, **kwargs):
        for json_entry in JsonStockData.objects.all():
            SqlStockData.objects.create(
                date=json_entry.date,
                trade_code=json_entry.trade_code,
                high=json_entry.high,
                low=json_entry.low,
                open=json_entry.open,
                close=json_entry.close,
                volume=json_entry.volume
            )
        self.stdout.write(self.style.SUCCESS('Successfully migrated data to SQL model'))
