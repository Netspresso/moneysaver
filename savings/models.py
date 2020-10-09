from django.db import models
from datetime import datetime
from django.db.models.functions import Extract


class Cel(models.Model):
    cel = models.CharField(max_length=120, blank=False, null=False)
    data = models.DateField(blank=False, null=False)
    kwota = models.FloatField(blank=False, null=False)

    # days = Extract(data, lookup_name='day').get()
    # start_date = datetime.datetime.strptime(self.request.data.get('today'),
    #                                         "%Y-%m-%d %H:%M")
    # end_date = datetime.datetime.strptime(self.request.data.get('dateDeDebut'),
    #                                       "%Y-%m-%d %H:%M")
    # diff = abs((end_date - start_date).days)
    # print(diff)

    def __str__(self):
        return self.cel