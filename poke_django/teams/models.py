from django.db import models
from trainer.models import Trainer

# Create your models here.
class Team(models.Model):
    """
    This model represents a Pokemon team. All pokemon teams
    must have a Trainer and can have 6 Pokemon or no Pokemon.
    """

    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    slot_1_dex_id = models.IntegerField(null=True, blank=True)
    slot_1_name = models.CharField(null=True, blank=True, max_length=150)

    slot_2_dex_id = models.IntegerField(null=True, blank=True)
    slot_2_name = models.CharField(null=True, blank=True, max_length=150)

    slot_3_dex_id = models.IntegerField(null=True, blank=True)
    slot_3_name = models.CharField(null=True, blank=True, max_length=150)

    slot_4_dex_id = models.IntegerField(null=True, blank=True)
    slot_4_name = models.CharField(null=True, blank=True, max_length=150)

    slot_5_dex_id = models.IntegerField(null=True, blank=True)
    slot_5_name = models.CharField(null=True, blank=True, max_length=150)

    slot_6_dex_id = models.IntegerField(null=True, blank=True)
    slot_6_name = models.CharField(null=True, blank=True, max_length=150)
