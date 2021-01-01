from django.test import TestCase
from rest_framework.test import APIClient
from teams.models import Team

class TeamDeletePokemonTestCase(TestCase):
    """
    Test set for deleting pokemons from the team
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

    def test_delete_pokemon_slot_1(self):
        """
        Deletes a pokemon from the designated team in slot 1.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 1

        pokemon_name = "Gastrodon"

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        response = self.client.delete("/teams/delete/{}/{}/".format(team_pk, str(slot)))
        self.assertEqual(response.status_code, 204)
        poke = Team.objects.get(pk=team_pk)
        self.assertFalse(poke.slot_1_national_dex_id)
        self.assertFalse(poke.slot_1_name)
        self.assertFalse(poke.slot_1_type_primary)
        self.assertFalse(poke.slot_1_type_secondary)
        self.assertFalse(poke.slot_1_type_height)
        self.assertFalse(poke.slot_1_type_weight)
        self.assertFalse(poke.slot_1_type_move_1)
        self.assertFalse(poke.slot_1_type_move_2)
        self.assertFalse(poke.slot_1_type_move_3)
        self.assertFalse(poke.slot_1_type_move_4)

    def test_delete_pokemon_slot_1_team_not_exists(self):
        """
        Tries to delete a pokemon from the designated team in slot 1. The team doesn't
        exists, Not Found error expected.
        """
        team_pk = "155555"
        slot = 1

        response = self.client.delete("/teams/delete/{}/{}/".format(team_pk, str(slot)))
        self.assertEqual(response.status_code, 404)

    def test_delete_pokemon_slot_1_not_exists(self):
        """
        Tries to delete a pokemon from the designated team in slot 1. The pokemon doesn't
        exists, since the slot is already empty, No content is expected.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 1

        response = self.client.delete("/teams/delete/{}/{}/".format(team_pk, str(slot)))
        self.assertEqual(response.status_code, 204)

    def test_delete_pokemon_slot_2(self):
        """
        Deletes a pokemon from the designated team in slot 2.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 2

        pokemon_name = "Gastrodon"

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        response = self.client.delete("/teams/delete/{}/{}/".format(team_pk, str(slot)))
        self.assertEqual(response.status_code, 204)
        poke = Team.objects.get(pk=team_pk)
        self.assertFalse(poke.slot_2_national_dex_id)
        self.assertFalse(poke.slot_2_name)
        self.assertFalse(poke.slot_2_type_primary)
        self.assertFalse(poke.slot_2_type_secondary)
        self.assertFalse(poke.slot_2_type_height)
        self.assertFalse(poke.slot_2_type_weight)
        self.assertFalse(poke.slot_2_type_move_1)
        self.assertFalse(poke.slot_2_type_move_2)
        self.assertFalse(poke.slot_2_type_move_3)
        self.assertFalse(poke.slot_2_type_move_4)

    def test_delete_pokemon_slot_2_team_not_exists(self):
        """
        Tries to delete a pokemon from the designated team in slot 2. The team doesn't
        exists, Not Found error expected.
        """
        team_pk = "155555"
        slot = 2

        response = self.client.delete("/teams/delete/{}/{}/".format(team_pk, str(slot)))
        self.assertEqual(response.status_code, 404)

    def test_delete_pokemon_slot_2_not_exists(self):
        """
        Tries to delete a pokemon from the designated team in slot 2. The pokemon doesn't
        exists, since the slot is already empty, No content is expected.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 2

        response = self.client.delete("/teams/delete/{}/{}/".format(team_pk, str(slot)))
        self.assertEqual(response.status_code, 204)

    def test_delete_pokemon_slot_3(self):
        """
        Deletes a pokemon from the designated team in slot 3.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 3

        pokemon_name = "Gastrodon"

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        response = self.client.delete("/teams/delete/{}/{}/".format(team_pk, str(slot)))
        self.assertEqual(response.status_code, 204)
        poke = Team.objects.get(pk=team_pk)
        self.assertFalse(poke.slot_3_national_dex_id)
        self.assertFalse(poke.slot_3_name)
        self.assertFalse(poke.slot_3_type_primary)
        self.assertFalse(poke.slot_3_type_secondary)
        self.assertFalse(poke.slot_3_type_height)
        self.assertFalse(poke.slot_3_type_weight)
        self.assertFalse(poke.slot_3_type_move_1)
        self.assertFalse(poke.slot_3_type_move_2)
        self.assertFalse(poke.slot_3_type_move_3)
        self.assertFalse(poke.slot_3_type_move_4)

    def test_delete_pokemon_slot_3_team_not_exists(self):
        """
        Tries to delete a pokemon from the designated team in slot 3. The team doesn't
        exists, Not Found error expected.
        """
        team_pk = "155555"
        slot = 3

        response = self.client.delete("/teams/delete/{}/{}/".format(team_pk, str(slot)))
        self.assertEqual(response.status_code, 404)

    def test_delete_pokemon_slot_3_not_exists(self):
        """
        Tries to delete a pokemon from the designated team in slot 3. The pokemon doesn't
        exists, since the slot is already empty, No content is expected.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 3

        response = self.client.delete("/teams/delete/{}/{}/".format(team_pk, str(slot)))
        self.assertEqual(response.status_code, 204)

    def test_delete_pokemon_slot_4(self):
        """
        Deletes a pokemon from the designated team in slot 4.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot  = 4

        pokemon_name = "Gastrodon"

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        response = self.client.delete("/teams/delete/{}/{}/".format(team_pk, str(slot)))
        self.assertEqual(response.status_code, 204)
        poke = Team.objects.get(pk=team_pk)
        self.assertFalse(poke.slot_4_national_dex_id)
        self.assertFalse(poke.slot_4_name)
        self.assertFalse(poke.slot_4_type_primary)
        self.assertFalse(poke.slot_4_type_secondary)
        self.assertFalse(poke.slot_4_type_height)
        self.assertFalse(poke.slot_4_type_weight)
        self.assertFalse(poke.slot_4_type_move_1)
        self.assertFalse(poke.slot_4_type_move_2)
        self.assertFalse(poke.slot_4_type_move_3)
        self.assertFalse(poke.slot_4_type_move_4)

    def test_delete_pokemon_slot_4_team_not_exists(self):
        """
        Tries to delete a pokemon from the designated team in slot 4. The team doesn't
        exists, Not Found error expected.
        """
        team_pk = "155555"
        slot  = 4

        response = self.client.delete("/teams/delete/{}/{}/".format(team_pk, str(slot)))
        self.assertEqual(response.status_code, 404)

    def test_delete_pokemon_slot_4_not_exists(self):
        """
        Tries to delete a pokemon from the designated team in slot 4. The pokemon doesn't
        exists, since the slot is already empty, No content is expected.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot  = 4

        response = self.client.delete("/teams/delete/{}/{}/".format(team_pk, str(slot)))
        self.assertEqual(response.status_code, 204)

    def test_delete_pokemon_slot_5(self):
        """
        Deletes a pokemon from the designated team in slot 5.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 5

        pokemon_name = "Gastrodon"

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        response = self.client.delete("/teams/delete/{}/{}/".format(team_pk, str(slot)))
        self.assertEqual(response.status_code, 204)
        poke = Team.objects.get(pk=team_pk)
        self.assertFalse(poke.slot_5_national_dex_id)
        self.assertFalse(poke.slot_5_name)
        self.assertFalse(poke.slot_5_type_primary)
        self.assertFalse(poke.slot_5_type_secondary)
        self.assertFalse(poke.slot_5_type_height)
        self.assertFalse(poke.slot_5_type_weight)
        self.assertFalse(poke.slot_5_type_move_1)
        self.assertFalse(poke.slot_5_type_move_2)
        self.assertFalse(poke.slot_5_type_move_3)
        self.assertFalse(poke.slot_5_type_move_4)

    def test_delete_pokemon_slot_5_team_not_exists(self):
        """
        Tries to delete a pokemon from the designated team in slot 5. The team doesn't
        exists, Not Found error expected.
        """
        team_pk = "155555"
        slot = 5

        response = self.client.delete("/teams/delete/{}/{}/".format(team_pk, str(slot)))
        self.assertEqual(response.status_code, 404)

    def test_delete_pokemon_slot_5_not_exists(self):
        """
        Tries to delete a pokemon from the designated team in slot 5. The pokemon doesn't
        exists, since the slot is already empty, No content is expected.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 5

        response = self.client.delete("/teams/delete/{}/{}/".format(team_pk, str(slot)))
        self.assertEqual(response.status_code, 204)

    def test_delete_pokemon_slot_6(self):
        """
        Deletes a pokemon from the designated team in slot 6.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 6

        pokemon_name = "Gastrodon"

        response = self.client.post("/teams/add/", {
                                                    "id":str(team_pk),
                                                    "slot": str(slot),
                                                    "pokemon_name": pokemon_name,
                                                    })

        response = self.client.delete("/teams/delete/{}/{}/".format(team_pk, str(slot)))
        self.assertEqual(response.status_code, 204)
        poke = Team.objects.get(pk=team_pk)
        self.assertFalse(poke.slot_6_national_dex_id)
        self.assertFalse(poke.slot_6_name)
        self.assertFalse(poke.slot_6_type_primary)
        self.assertFalse(poke.slot_6_type_secondary)
        self.assertFalse(poke.slot_6_type_height)
        self.assertFalse(poke.slot_6_type_weight)
        self.assertFalse(poke.slot_6_type_move_1)
        self.assertFalse(poke.slot_6_type_move_2)
        self.assertFalse(poke.slot_6_type_move_3)
        self.assertFalse(poke.slot_6_type_move_4)

    def test_delete_pokemon_slot_6_team_not_exists(self):
        """
        Tries to delete a pokemon from the designated team in slot 6. The team doesn't
        exists, Not Found error expected.
        """
        team_pk = "155555"
        slot = 6

        response = self.client.delete("/teams/delete/{}/{}/".format(team_pk, str(slot)))
        self.assertEqual(response.status_code, 404)

    def test_delete_pokemon_slot_6_not_exists(self):
        """
        Tries to delete a pokemon from the designated team in slot 6. The pokemon doesn't
        exists, since the slot is already empty, No content is expected.
        """
        response = self.client.post("/teams/create/",
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]
        slot = 6

        response = self.client.delete("/teams/delete/{}/{}/".format(team_pk, str(slot)))
        self.assertEqual(response.status_code, 204)
