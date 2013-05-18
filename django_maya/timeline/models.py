from django.db import models

# Create your models here.
'''
class Header(models.Model):
	place = models.CharField(max_length = 50)
	event = models.CharField(max_length = 50)
	likes = models.IntegerField()
	posts = models.IntegerField()
'''

class Location(models.Model):
	name = models.CharField(max_length = 50)
	
class Message(models.Model):
	location = models.ForeignKey(Location)
	event = models.CharField(max_length = 50, default = '')
	img = models.URLField(default = '')
	comment = models.CharField(max_length = 5000, default = '')
	time = models.DateTimeField(auto_now_add = True)
	likes = models.IntegerField(default = 0)
