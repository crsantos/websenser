from django.db import models
from django.contrib.auth.models import User

class Sensor(models.Model):
    """(Sensor description)"""
    
    name = models.CharField(blank=True, max_length=100)
    
    def __unicode__(self):
        return self.name
    

class Measurement(models.Model):
    """(Measurement description)"""
    
    measure = models.CharField(blank=True, max_length=100)
    user = models.ForeignKey(User)
    sensor = models.ForeignKey(Sensor)
    
    def __unicode__(self):
        return u"%s - %s" % (self.sensor.name,self.measure)
    

