from django.test import TestCase
from rest_framework.test import APIClient
from teams.models import Team

class GetallTeamsPokemonTestCase(TestCase):
    """
    Test set for deleting pokemons from the team
    """
    client = APIClient()
    trainer_id_0 = 0
    trainer_id_1 = 0
    trainer_id_2 = 0
    team_id_1 = 0
    team_id_2 = []

    def setUp(self):
        """
        Set up case. Creates some test data:
        A trainer with no teams.
        A trainer with one team.
        A trainer with two teams.
        """
        # No teams trainer
        response = self.client.post('/trainer/create/',
        {"name": "Blue",
         "las_name": "Oak"})
        self.trainer_id_0 = response.json()["id"]

        # A Trainer with one Team
        response = self.client.post('/trainer/create/',
        {"name": "Some",
         "las_name": "Dude"})
        self.trainer_id_1 = response.json()["id"]

        response = self.client.post('/teams/create/', {"trainer": str(self.trainer_id_1)})
        self.team_id_1 = response.json()["id"]

        # A trainer, 2 teams
        response = self.client.post('/trainer/create/',
        {"name": "Another",
         "las_name": "One"})
        self.trainer_id_2 = response.json()["id"]

        response = self.client.post('/teams/create/', {"trainer": str(self.trainer_id_2)})
        self.team_id_2.append(response.json()["id"])
        response = self.client.post('/teams/create/', {"trainer": str(self.trainer_id_2)})
        self.team_id_2.append(response.json()["id"])

    def test_getall_teams_no_teams_exist(self):
        """
        When sending a request with an id of a trainer that has no teams, a message
        that says: "No teams found" and a status code 204 No Content is expected.
        """
        response = self.client.get("/teams/getall/{}/".format(self.trainer_id_0))
        self.assertEqual(response.status_code, 204)

    def test_getall_teams_trainer_has_one_team(self):
        """
        When sending a request with an id of a trainer that has one team, one
        team with empty pokemon slots is expected and a status code 200 Ok is expected.
        """
        response = self.client.get("/teams/getall/{}/".format(self.trainer_id_1))
        self.assertEqual(response.status_code, 200)
        team = Team.objects.get(pk=self.team_id_1)
        self.assertEqual(response.json()[0]["id"], team.id)

    def test_getall_teams_trainer_has_multiple_teams(self):
        """
        When sending a request with an id of a trainer that has multiple teams, a
        response with multiple teams, one in each index is expected and a status code 200.
        """
        response = self.client.get("/teams/getall/{}/".format(self.trainer_id_2))
        self.assertEqual(response.status_code, 200)
        teams = Team.objects.filter(trainer=self.trainer_id_2)
        list_of_team_ids = [team.id for team in teams]
        self.assertIn(response.json()[0]["id"], list_of_team_ids)
        self.assertIn(response.json()[1]["id"], list_of_team_ids)
