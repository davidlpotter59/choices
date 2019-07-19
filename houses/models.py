from django.db import models

# Create your models here.
class House(models.Model):
    house_name = models.CharField(max_length=50, default=0)

# def __str__(self):
#         return u'{0}'.format(self.house_name)

# def __unicode__(self):
    def __str__(self):
    # return '%s' % self.house_name
        return self.house_name
