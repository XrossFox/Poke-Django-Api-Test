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
        poke = Team.objects.get(pk=team_pk)
        self.assertEqual(poke.slot_1_pokemon.national_dex_id, national_dex_id)
        self.assertEqual(poke.slot_1_pokemon.name, pokemon_name.lower())
        self.assertEqual(poke.slot_1_pokemon.type_primary, type_1)
        self.assertEqual(poke.slot_1_pokemon.type_secondary, type_2)

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
        poke = Team.objects.get(pk=team_pk)
        self.assertEqual(poke.slot_1_pokemon.national_dex_id, national_dex_id)
        self.assertEqual(poke.slot_1_pokemon.name, pokemon_name.lower())
        self.assertEqual(poke.slot_1_pokemon.type_primary, type_1)
        self.assertEqual(poke.slot_1_pokemon.type_secondary, type_2)

    def test_add_pokemon_slot_1_not_exist(self):
        """
        tries to add a pokemon that doesn't exist. A Not Found error is expected.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 1
        pokemon_name = "Agumon"

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        self.assertEqual(response.status_code, 404)

    def test_add_pokemon_slot_2_1_type(self):
        """
        Adds a new pokemon to Slot 2. Expected code: 201.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 2
        pokemon_name = "Zangoose"
        national_dex_id = 335
        type_1 = "normal"
        type_2 = None

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        self.assertEqual(response.status_code, 201)
        poke = Team.objects.get(pk=team_pk)
        self.assertEqual(poke.slot_2_pokemon.national_dex_id, national_dex_id)
        self.assertEqual(poke.slot_2_pokemon.name, pokemon_name.lower())
        self.assertEqual(poke.slot_2_pokemon.type_primary, type_1)
        self.assertEqual(poke.slot_2_pokemon.type_secondary, type_2)

    def test_add_pokemon_slot_2_2_type(self):
        """
        Adds a new pokemon to Slot 1. Expected code: 201.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 2
        pokemon_name = "Houndoom"
        national_dex_id = 229
        type_1 = "dark"
        type_2 = "fire"

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        self.assertEqual(response.status_code, 201)
        poke = Team.objects.get(pk=team_pk)
        self.assertEqual(poke.slot_2_pokemon.national_dex_id, national_dex_id)
        self.assertEqual(poke.slot_2_pokemon.name, pokemon_name.lower())
        self.assertEqual(poke.slot_2_pokemon.type_primary, type_1)
        self.assertEqual(poke.slot_2_pokemon.type_secondary, type_2)

    def test_add_pokemon_slot_2_not_exist(self):
        """
        tries to add a pokemon that doesn't exist. A Not Found error is expected.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 2
        pokemon_name = "Gabumon"

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        self.assertEqual(response.status_code, 404)

    def test_add_pokemon_slot_3_1_type(self):
        """
        Adds a new pokemon to Slot 3. Expected code: 201.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 3
        pokemon_name = "Zigzagoon"
        national_dex_id = 263
        type_1 = "normal"
        type_2 = None

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        self.assertEqual(response.status_code, 201)
        poke = Team.objects.get(pk=team_pk)
        self.assertEqual(poke.slot_3_pokemon.national_dex_id, national_dex_id)
        self.assertEqual(poke.slot_3_pokemon.name, pokemon_name.lower())
        self.assertEqual(poke.slot_3_pokemon.type_primary, type_1)
        self.assertEqual(poke.slot_3_pokemon.type_secondary, type_2)

    def test_add_pokemon_slot_3_2_type(self):
        """
        Adds a new pokemon to Slot 3. Expected code: 201.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 3
        pokemon_name = "Gastrodon"
        national_dex_id = 423
        type_1 = "water"
        type_2 = "ground"

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        self.assertEqual(response.status_code, 201)
        poke = Team.objects.get(pk=team_pk)
        self.assertEqual(poke.slot_3_pokemon.national_dex_id, national_dex_id)
        self.assertEqual(poke.slot_3_pokemon.name, pokemon_name.lower())
        self.assertEqual(poke.slot_3_pokemon.type_primary, type_1)
        self.assertEqual(poke.slot_3_pokemon.type_secondary, type_2)

    def test_add_pokemon_slot_3_not_exist(self):
        """
        tries to add a pokemon that doesn't exist to Slot 3. A Not Found error is expected.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 3
        pokemon_name = "Patamon"

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        self.assertEqual(response.status_code, 404)

    def test_add_pokemon_slot_4_1_type(self):
        """
        Adds a new pokemon to Slot 4. Expected code: 201.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 4
        pokemon_name = "Zigzagoon"
        national_dex_id = 263
        type_1 = "normal"
        type_2 = None

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        self.assertEqual(response.status_code, 201)
        poke = Team.objects.get(pk=team_pk)
        self.assertEqual(poke.slot_4_pokemon.national_dex_id, national_dex_id)
        self.assertEqual(poke.slot_4_pokemon.name, pokemon_name.lower())
        self.assertEqual(poke.slot_4_pokemon.type_primary, type_1)
        self.assertEqual(poke.slot_4_pokemon.type_secondary, type_2)

    def test_add_pokemon_slot_4_2_type(self):
        """
        Adds a new pokemon to Slot 4. Expected code: 201.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 4
        pokemon_name = "Gastrodon"
        national_dex_id = 423
        type_1 = "water"
        type_2 = "ground"

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        self.assertEqual(response.status_code, 201)
        poke = Team.objects.get(pk=team_pk)
        self.assertEqual(poke.slot_4_pokemon.national_dex_id, national_dex_id)
        self.assertEqual(poke.slot_4_pokemon.name, pokemon_name.lower())
        self.assertEqual(poke.slot_4_pokemon.type_primary, type_1)
        self.assertEqual(poke.slot_4_pokemon.type_secondary, type_2)

    def test_add_pokemon_slot_4_not_exist(self):
        """
        tries to add a pokemon that doesn't exist to Slot 4. A Not Found error is expected.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 4
        pokemon_name = "Patamon"

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        self.assertEqual(response.status_code, 404)

    def test_add_pokemon_slot_5_1_type(self):
        """
        Adds a new pokemon to Slot 5. Expected code: 201.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 5
        pokemon_name = "Zigzagoon"
        national_dex_id = 263
        type_1 = "normal"
        type_2 = None

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        self.assertEqual(response.status_code, 201)
        poke = Team.objects.get(pk=team_pk)
        self.assertEqual(poke.slot_5_pokemon.national_dex_id, national_dex_id)
        self.assertEqual(poke.slot_5_pokemon.name, pokemon_name.lower())
        self.assertEqual(poke.slot_5_pokemon.type_primary, type_1)
        self.assertEqual(poke.slot_5_pokemon.type_secondary, type_2)

    def test_add_pokemon_slot_5_2_type(self):
        """
        Adds a new pokemon to Slot 5. Expected code: 201.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 5
        pokemon_name = "Gastrodon"
        national_dex_id = 423
        type_1 = "water"
        type_2 = "ground"

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        self.assertEqual(response.status_code, 201)
        poke = Team.objects.get(pk=team_pk)
        self.assertEqual(poke.slot_5_pokemon.national_dex_id, national_dex_id)
        self.assertEqual(poke.slot_5_pokemon.name, pokemon_name.lower())
        self.assertEqual(poke.slot_5_pokemon.type_primary, type_1)
        self.assertEqual(poke.slot_5_pokemon.type_secondary, type_2)

    def test_add_pokemon_slot_5_not_exist(self):
        """
        tries to add a pokemon that doesn't exist to Slot 5. A Not Found error is expected.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 5
        pokemon_name = "Patamon"

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        self.assertEqual(response.status_code, 404)

    def test_add_pokemon_slot_6_1_type(self):
        """
        Adds a new pokemon to Slot 6. Expected code: 201.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 6
        pokemon_name = "Zigzagoon"
        national_dex_id = 263
        type_1 = "normal"
        type_2 = None

        response = self.client.post("/teams/add/", {
                                                    "id": str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        self.assertEqual(response.status_code, 201)
        poke = Team.objects.get(pk=team_pk)
        self.assertEqual(poke.slot_6_pokemon.national_dex_id, national_dex_id)
        self.assertEqual(poke.slot_6_pokemon.name, pokemon_name.lower())
        self.assertEqual(poke.slot_6_pokemon.type_primary, type_1)
        self.assertEqual(poke.slot_6_pokemon.type_secondary, type_2)

    def test_add_pokemon_slot_6_2_type(self):
        """
        Adds a new pokemon to Slot 6. Expected code: 201.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 6
        pokemon_name = "Gastrodon"
        national_dex_id = 423
        type_1 = "water"
        type_2 = "ground"

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        self.assertEqual(response.status_code, 201)
        poke = Team.objects.get(pk=team_pk)
        self.assertEqual(poke.slot_6_pokemon.national_dex_id, national_dex_id)
        self.assertEqual(poke.slot_6_pokemon.name, pokemon_name.lower())
        self.assertEqual(poke.slot_6_pokemon.type_primary, type_1)
        self.assertEqual(poke.slot_6_pokemon.type_secondary, type_2)

    def test_add_pokemon_slot_6_not_exist(self):
        """
        tries to add a pokemon that doesn't exist to Slot 6. A Not Found error is expected.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 6
        pokemon_name = "Patamon"

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        self.assertEqual(response.status_code, 404)
