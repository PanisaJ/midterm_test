from django.db import models

class Statistic(models.Model):
    number = models.IntegerField(default=0)
    times = models.IntegerField(default=0)
    def __int__(self):
        return self.number
