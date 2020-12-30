from django.db import models
from trainer.models import Trainer

# Create your models here.
class Team(models.Model):
    """
    This model represents a Pokemon team. All pokemon teams
    must have a Trainer and can have 6 Pokemon or no Pokemon.
    """

    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    slot_1_national_dex_id = models.IntegerField(null=True, blank=True)
    slot_1_name = models.CharField(null=True, blank=True, max_length=150)
    slot_1_type_primary = models.CharField(null=True, blank=True, max_length=150)
    slot_1_type_secondary = models.CharField(null=True, blank=True, max_length=150)
    slot_1_type_species = models.CharField(null=True, blank=True, max_length=150)
    slot_1_type_height = models.IntegerField(null = True)
    slot_1_type_weight = models.IntegerField(null = True)
    slot_1_type_move_1 = models.CharField(null=True, blank=True, max_length=150)
    slot_1_type_move_2 = models.CharField(null=True, blank=True, max_length=150)
    slot_1_type_move_3 = models.CharField(null=True, blank=True, max_length=150)
    slot_1_type_move_4 = models.CharField(null=True, blank=True, max_length=150)


    slot_2_national_dex_id = models.IntegerField(null=True, blank=True)
    slot_2_name = models.CharField(null=True, blank=True, max_length=150)
    slot_2_type_primary = models.CharField(null=True, blank=True, max_length=150)
    slot_2_type_secondary = models.CharField(null=True, blank=True, max_length=150)
    slot_2_type_species = models.CharField(null=True, blank=True, max_length=150)
    slot_2_type_height = models.IntegerField(null = True)
    slot_2_type_weight = models.IntegerField(null = True)
    slot_2_type_move_1 = models.CharField(null=True, blank=True, max_length=150)
    slot_2_type_move_2 = models.CharField(null=True, blank=True, max_length=150)
    slot_2_type_move_3 = models.CharField(null=True, blank=True, max_length=150)
    slot_2_type_move_4 = models.CharField(null=True, blank=True, max_length=150)

    slot_3_national_dex_id = models.IntegerField(null=True, blank=True)
    slot_3_name = models.CharField(null=True, blank=True, max_length=150)
    slot_3_type_primary = models.CharField(null=True, blank=True, max_length=150)
    slot_3_type_secondary = models.CharField(null=True, blank=True, max_length=150)
    slot_3_type_species = models.CharField(null=True, blank=True, max_length=150)
    slot_3_type_height = models.IntegerField(null = True)
    slot_3_type_weight = models.IntegerField(null = True)
    slot_3_type_move_1 = models.CharField(null=True, blank=True, max_length=150)
    slot_3_type_move_2 = models.CharField(null=True, blank=True, max_length=150)
    slot_3_type_move_3 = models.CharField(null=True, blank=True, max_length=150)
    slot_3_type_move_4 = models.CharField(null=True, blank=True, max_length=150)

    slot_4_national_dex_id = models.IntegerField(null=True, blank=True)
    slot_4_name = models.CharField(null=True, blank=True, max_length=150)
    slot_4_type_primary = models.CharField(null=True, blank=True, max_length=150)
    slot_4_type_secondary = models.CharField(null=True, blank=True, max_length=150)
    slot_4_type_species = models.CharField(null=True, blank=True, max_length=150)
    slot_4_type_height = models.IntegerField(null = True)
    slot_4_type_weight = models.IntegerField(null = True)
    slot_4_type_move_1 = models.CharField(null=True, blank=True, max_length=150)
    slot_4_type_move_2 = models.CharField(null=True, blank=True, max_length=150)
    slot_4_type_move_3 = models.CharField(null=True, blank=True, max_length=150)
    slot_4_type_move_4 = models.CharField(null=True, blank=True, max_length=150)

    slot_5_national_dex_id = models.IntegerField(null=True, blank=True)
    slot_5_name = models.CharField(null=True, blank=True, max_length=150)
    slot_5_type_primary = models.CharField(null=True, blank=True, max_length=150)
    slot_5_type_secondary = models.CharField(null=True, blank=True, max_length=150)
    slot_5_type_species = models.CharField(null=True, blank=True, max_length=150)
    slot_5_type_height = models.IntegerField(null = True)
    slot_5_type_weight = models.IntegerField(null = True)
    slot_5_type_move_1 = models.CharField(null=True, blank=True, max_length=150)
    slot_5_type_move_2 = models.CharField(null=True, blank=True, max_length=150)
    slot_5_type_move_3 = models.CharField(null=True, blank=True, max_length=150)
    slot_5_type_move_4 = models.CharField(null=True, blank=True, max_length=150)

    slot_6_national_dex_id = models.IntegerField(null=True, blank=True)
    slot_6_name = models.CharField(null=True, blank=True, max_length=150)
    slot_6_type_primary = models.CharField(null=True, blank=True, max_length=150)
    slot_6_type_secondary = models.CharField(null=True, blank=True, max_length=150)
    slot_6_type_species = models.CharField(null=True, blank=True, max_length=150)
    slot_6_type_height = models.IntegerField(null = True)
    slot_6_type_weight = models.IntegerField(null = True)
    slot_6_type_move_1 = models.CharField(null=True, blank=True, max_length=150)
    slot_6_type_move_2 = models.CharField(null=True, blank=True, max_length=150)
    slot_6_type_move_3 = models.CharField(null=True, blank=True, max_length=150)
    slot_6_type_move_4 = models.CharField(null=True, blank=True, max_length=150)
