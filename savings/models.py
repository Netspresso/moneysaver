from django.db import models


class Aim(models.Model):
    aim = models.CharField(max_length=120, blank=False, null=False)
    data = models.DateField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    isFinished = models.BooleanField(default=False)

    owner = models.ForeignKey('auth.User',
                              related_name='aims',
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.aim
