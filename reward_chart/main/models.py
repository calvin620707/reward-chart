from django.db import models


class Chart(models.Model):
    name = models.CharField(max_length=128)
    points = models.IntegerField(default=0)
    modified = models.DateTimeField("Last modified date time", auto_now=True)
