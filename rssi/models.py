
from django.db import models
class Rssi(models.Model):
    value=models.DecimalField(max_digits=10,decimal_places=3)

    