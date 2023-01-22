from django.db import models

# Create your models here.

class Exchange(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self) -> str:
        return f'{self.id} {self.name}'


class Pair(models.Model):
    symbol = models.CharField(max_length=20)
    ask = models.FloatField()
    bid = models.FloatField()
    exchange = models.ForeignKey(Exchange, on_delete=models.PROTECT)
    def __str__(self) -> str:
        return f'ID: {self.id} Symbol: {self.symbol} Ask: {self.ask} Bid: {self.bid} Exchange: {self.exchange}'
