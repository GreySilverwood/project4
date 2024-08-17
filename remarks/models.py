from django.db import models

# Create your models here.
class Remark (models.Model):
    title = models.CharField(max_length = 200)
    comments = models.TextField(max_length = 2000)
    rating = models.PositiveIntegerField()

    def __str__(self): 
        return self.title