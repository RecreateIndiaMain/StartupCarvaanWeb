
from django.db import models
class Rssi(models.Model):
    id=models.AutoField(primary_key=True)
    value=models.DecimalField(max_digits=10,decimal_places=3)
    