from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone


class Statistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    gender = models.CharField(
        max_length=9, choices=[('male', 'male'), ('female', 'female')], default='male')
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str((self.user.username, self.weight, self.height, self.age, self.gender, self.timestamp))
