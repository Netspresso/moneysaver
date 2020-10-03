from django.db import models


class Cel(models.Model):
    cel = models.CharField(max_length=120, blank=False, null=False)
    data = models.DateField(blank=False, null=False)
    kwota = models.FloatField(blank=False, null=False)

    def __str__(self):
        return self.cel