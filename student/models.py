from django.db import models

# Create your models here.
from houses.models import House

class Student(models.Model):
    name = models.CharField(max_length=50, default=0)
    house = models.ForeignKey(House, related_name='house', on_delete=models.SET_NULL, null=True)

    # def __unicode__(self):
    #   return '%s' % self.house