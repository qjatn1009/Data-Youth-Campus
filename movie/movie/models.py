from django.db import models

# Create your models here.
class naver_movie(models.Model):
    nickname = models.CharField(max_length=100)
    score = models.IntegerField()
    movie_name = models.CharField(max_length=100)

class naver_keyword(models.Model):
    title = models.CharField(max_length=100)
    URL = models.CharField(max_length=100)
    summary = models.CharField(max_length=100)