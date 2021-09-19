from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=20)
    game = models.CharField(max_length=20)
    score = models.IntegerField()


