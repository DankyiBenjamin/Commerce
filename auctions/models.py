from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionList(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    starting_bid = models.IntegerField()
    current_bid = models.IntegerField()
    image_url = models.CharField()
    


class Bids(models.Model):
    pass


class Comments(models.Model):
    pass


class Watchlist(models.Model):
    pass