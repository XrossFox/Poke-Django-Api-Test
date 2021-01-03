from django.db import models
from trainer.models import Trainer

# Create your models here.
class Team(models.Model):
    """
    This model represents a Pokemon team. All pokemon teams
    must have a Trainer and can have 6 Pokemon or no Pokemon.
    """

    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    slot_1_pokemon = models.ForeignKey("Pokemon", null=True, blank=True,
                                        on_delete=models.SET_NULL, related_name="pokemon_1")
    slot_2_pokemon = models.ForeignKey("Pokemon", null=True, blank=True,
                                        on_delete=models.SET_NULL, related_name="pokemon_2")
    slot_3_pokemon = models.ForeignKey("Pokemon", null=True, blank=True,
                                        on_delete=models.SET_NULL, related_name="pokemon_3")
    slot_4_pokemon = models.ForeignKey("Pokemon", null=True, blank=True,
                                        on_delete=models.SET_NULL, related_name="pokemon_4")
    slot_5_pokemon = models.ForeignKey("Pokemon", null=True, blank=True,
                                        on_delete=models.SET_NULL, related_name="pokemon_5")
    slot_6_pokemon = models.ForeignKey("Pokemon", null=True, blank=True,
                                        on_delete=models.SET_NULL, related_name="pokemon_6")

class Pokemon(models.Model):
    """
    Model that represents the pokemon in the Team model.
    """
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    national_dex_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(null=True, blank=True, max_length=150)
    type_primary = models.CharField(null=True, blank=True, max_length=150)
    type_secondary = models.CharField(null=True, blank=True, max_length=150)
    species = models.CharField(null=True, blank=True, max_length=150)
    height = models.IntegerField(null = True)
    weight = models.IntegerField(null = True)
    move_1 = models.CharField(null=True, blank=True, max_length=150)
    move_2 = models.CharField(null=True, blank=True, max_length=150)
    move_3 = models.CharField(null=True, blank=True, max_length=150)
    move_4 = models.CharField(null=True, blank=True, max_length=150)
