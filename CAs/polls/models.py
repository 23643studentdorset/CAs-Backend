import datetime
from django.db import models
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    score = models.IntegerField()

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Movie, on_delete=models.CASCADE)
    choice = models.IntegerField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice
