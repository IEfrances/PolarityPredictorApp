from django.db import models


class MovieReview(models.Model):
    image_url = models.URLField(null=True)
    review = models.TextField()
    predicted_sentiment  = models.CharField(max_length=10)

