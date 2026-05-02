from django.db import models

class Review(models.Model):
	# required
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	rating = models.IntegerField()
	
	body = models.TextField(blank=True) # allow blank
