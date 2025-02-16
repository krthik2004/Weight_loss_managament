# weight/models.py

from django.db import models
from django.contrib.auth.models import User

class WeightUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class WeightRecord(models.Model):
    user = models.ForeignKey(WeightUser, on_delete=models.CASCADE)
    weight = models.FloatField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username} - {self.weight} kg on {self.date_added}"
