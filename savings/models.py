from django.db import models
# from datetime import datetime
# from django.db.models.functions import Extract


class Aim(models.Model):
    aim = models.CharField(max_length=120, blank=False, null=False)
    data = models.DateField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False)

    def __str__(self):
        return self.aim
