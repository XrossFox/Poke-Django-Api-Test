from django.test import TestCase
from rest_framework.test import APIClient
from teams.models import Team

class TeamAddPokemonTestCase(TestCase):
    """
    Test set for adding pokemons for the team
    """
    client = APIClient()
    trainer_id = 0
    team_id = 0

    def setUp(self):
        """
        Set up case. Creates a trainer to work with.
        """
        response = self.client.post('/trainer/create/',
        {"name": "Blue",
         "las_name": "Oak"})
        self.trainer_id = response.json()["id"]

    def test_add_pokemon_slot_1_1_type(self):
        """
        Adds a new pokemon to Slot 1. Expected code: 201.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 1
        pokemon_name = "Typhlosion"
        national_dex_id = 157
        type_1 = "fire"
        type_2 = None

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        self.assertEqual(response.status_code, 201)
        poke = Team.objects.get(pk=self.team_id)
        self.assertEqual(poke.slot_1_national_dex_id, national_dex_id)
        self.assertEqual(poke.slot_1_name, pokemon_name.lower())
        self.assertEqual(poke.slot_1_type_primary, type_1)
        self.assertEqual(poke.slot_1_type_secondary, type_2)

    def test_add_pokemon_slot_1_2_type(self):
        """
        Adds a new pokemon to Slot 1. Expected code: 201.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 1
        pokemon_name = "Tyranitar"
        national_dex_id = 248
        type_1 = "rock"
        type_2 = "dark"

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        self.assertEqual(response.status_code, 201)
        poke = Team.objects.get(pk=self.team_id)
        self.assertEqual(poke.slot_1_national_dex_id, national_dex_id)
        self.assertEqual(poke.slot_1_name, pokemon_name.lower())
        self.assertEqual(poke.slot_1_type_primary, type_1)
        self.assertEqual(poke.slot_1_type_secondary, type_2)
