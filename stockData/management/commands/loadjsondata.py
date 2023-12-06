import json
from django.core.management.base import BaseCommand
from stockData.models import JsonStockData

class Command(BaseCommand):
    help = 'Load a JSON file into the database'

    def handle(self, *args, **kwargs):
        with open('F:\py_project\stockMarketApp\\stock_market_data.json', 'r') as file:
            data = json.load(file)
            for entry in data:
                JsonStockData.objects.create(
                    date=entry['date'],
                    trade_code=entry['trade_code'],
                    high=entry['high'].replace(',', ''), 
                    low=entry['low'].replace(',', ''),
                    open=entry['open'].replace(',', ''),
                    close=entry['close'].replace(',', ''),
                    #volume=entry['volume'].replace(',', '')
                    volume=entry['volume']
                )
