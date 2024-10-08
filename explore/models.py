import uuid

from django.db import models

class Food(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    image = models.URLField()
    description = models.TextField()
    ingredients = models.TextField()
    food_type = models.CharField(max_length=20)
