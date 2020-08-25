from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class news(models.Model):
    title = models.CharField(max_length = 200)
    url = models.CharField(max_length = 2000)
    index = models.IntegerField(default=0)
    img_index = models.CharField(default =' ',max_length = 200)

class premier_league(models.Model):
    team = models.CharField(max_length = 200)
    point = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    play =models.IntegerField(default=0)
    gdp = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    idx = models.CharField(default='normal',max_length=200)
    
    def __str__(self):
        return self.team