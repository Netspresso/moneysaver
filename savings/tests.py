from django.test import TestCase
from datetime import datetime
from django.db.models.functions import Extract

date = datetime(2021, 1, 11)

day = Extract(date, 'day')
print(day)
