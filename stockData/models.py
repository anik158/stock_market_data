
from django.db import models

# Model for JSON data
class JsonStockData(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=100)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    open = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.CharField(max_length=100) 

# Model for SQL data
class SqlStockData(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=100)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    open = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    #volume = models.BigIntegerField()
    volume = models.CharField(max_length=100) 
