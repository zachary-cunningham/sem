from django.db import models

class Review(models.Model):
	# required
	title = models.CharField()
	author = models.CharField()
	rating = models.IntegerField()
	
	body = models.TextField(blank=True) # allow blank
