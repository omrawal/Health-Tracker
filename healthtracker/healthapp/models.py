from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Statistic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    # 0 = male
    # 1 = female
    gender = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.user.username, self.weight, self.height, self.age, self.gender, self.timestamp)
