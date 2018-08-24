from django.db import models
from django.utils import timezone


# Create your models here.
class Alcohol(models.Model):
    name = models.CharField(max_length=20)
    dosu = models.FloatField()
    quantity = models.IntegerField()
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return '<술이름: {}, 도수: {},먹은 양: {}>'.format(self.name,self.dosu,self.quantity)