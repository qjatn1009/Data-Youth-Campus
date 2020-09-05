from django.db import models
# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=10, primary_key= True, null = False, default= "정보없음")
    pw = models.CharField(max_length=20, null = False , default= "123123")
    happy = models.FloatField(max_length=10)
    sad = models.FloatField(max_length=10)
    angry = models.FloatField(max_length=10)
    surprised = models.FloatField(max_length=10)
    user_category = models.CharField(max_length=100, null= True)
    
    def __str__(self):
        return self.user_id

class seomyeon(models.Model):
    store_name = models.CharField(max_length=50, primary_key=True)
    store_category = models.CharField(max_length = 50)
    url = models.CharField(max_length= 50)
    x = models.FloatField(max_length=10, default= 0)
    y = models.FloatField(max_length=10, default= 0)
    search_word = models.CharField(max_length= 50, null= True)
    hashtags = models.CharField(max_length= 400, null= True)
    menu = models.CharField(max_length= 4000, null= True)
    likes = models.IntegerField(default= 0)    
    sentiment = models.FloatField(max_length=10, default= 0)
    store_happy = models.FloatField(max_length=10, default= 0)
    store_sad = models.FloatField(max_length=10, default= 0)
    store_angry = models.FloatField(max_length=10, default= 0)
    store_surprised = models.FloatField(max_length=10, default= 0)
    count = models.IntegerField(default= 0)
    WEIGHTED_VOTE = models.FloatField(max_length=10, default= 0)

    def __str__(self):
        return self.store_name