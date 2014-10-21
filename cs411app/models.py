from django.db import models

# Create your models here.
class Transaction(models.Model):
    trade = models.ForeignKey(Trade)
    wants = models.ManyToManyField(Item)
    offers = models.ManyToManyField(Item)

class Trade(models.Model):
    time = models.DateTimeField()

    guid = models.IntegerField(max_length=11, primary_key=True)

# Base class for items
class Item(models.Model):
    id = models.IntegerField(max_length=64, primary_key=True)

# Additional class for customizable items
class CustomizableItem(Item):
    vintage = models.BooleanField(default=False)
    level = models.IntegerField(max_length=3)
    unusualEffects = models.CharField(null=True) # Only applies for some items
    customizers = models.ManyToManyField(CustomizerItem)

# TODO CRON-job for trade updates - use bazaar.tf for now
    # OHFUCK We need to get NLP parsing working
    # For now maybe just display trades?
# TODO Update ER Diagram/Relation list to reflect this
# TODO Actually throw this up on LOLPHP (via GAE most likely)