from .models import Review
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class ReviewSerializer(ModelSerializer):
	body = serializers.CharField(required=False, allow_blank=True, default="")

	class Meta:
		model = Review
		fields = ['id', 'title', 'author', 'rating', 'body']