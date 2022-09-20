from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    film_watched    = models.CharField(max_length=255)
    film_title      = models.TextField()
    film_rating     = models.TextField()
    release_date    = models.TextField()
    film_review     = models.TextField()
    