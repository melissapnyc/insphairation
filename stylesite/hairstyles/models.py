from django.db import models
from django import forms

class Style(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    length = models.CharField(max_length=50)
    texture = models.CharField(max_length=50)
    time_of_day = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name
    
class Image(models.Model):
    style = models.ForeignKey(Style)
    image = models.CharField(max_length=1000)
    
    def __unicode__(self):
        return self.image