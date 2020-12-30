from django.test import TestCase
from rest_framework.test import APIClient
from teams.models import Team

class TeamTestCase(TestCase):
    """
    Test set for Team CRD (there is no update here)
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

    def test_create_team(self):
        """
        Creates a new team for the trainer. Asserts that
        the team is created.
        """
        response = self.client.post("/teams/create/", 
        {
            "trainer": str(self.trainer_id),
        })

        self.assertEqual(response.status_code, 201)
        self.team_id = response.json()["id"]
        team = Team.objects.get(pk=self.team_id,
                                trainer=self.trainer_id)
        self.assertAlmostEqual(self.trainer_id, team.trainer.pk)

    def test_create_team_empty_data(self):
        """
        Tries to create a team with an empty json.
        Expects a bad request error.
        """
        response = self.client.post("/teams/create/", 
        {   
        })

        self.assertEqual(response.status_code, 400)

    def test_create_team_bad_data(self):
        """
        Tries to create a team with bad data.
        Expects a bad request error.
        """
        response = self.client.post("/teams/create/", 
        {   
            "Pokemon_Master": str(self.trainer_id),
        })

        self.assertEqual(response.status_code, 400)

    def test_create_team_trainer_not_exist(self):
        """
        Tries to create a team with a trainer that doesn't
        exists. Expects a bad request error.
        """
        response = self.client.post("/teams/create/", 
        {
            "trainer": "2",
        })

        self.assertEqual(response.status_code, 400)

    def test_get_team(self):
        """
        Retrieves a team using the team pk. Expects
        a 200 code.
        """
        response = self.client.post("/teams/create/", 
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]

        response = self.client.get(
            "/teams/get/"+str(team_pk)+"/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], team_pk)
        self.assertEqual(
            response.json()["trainer"], self.trainer_id)

    def test_get_team_bad_id(self):
        """
        Tries to retrieve a team that doesn't exist.
        Error not found expected.
        """
        response = self.client.get(
            "/teams/get/15555/")
        self.assertEqual(response.status_code, 404)

    def test_get_team_bad_param(self):
        """
        Tries to retrieve a team with the wrong type of
        path param, a string instead of a number.
        Error not found expected.
        """
        response = self.client.get(
            "/teams/get/15555/")
        self.assertEqual(response.status_code, 404)

    def test_delete_team(self):
        """
        Deletes an existing team. Code 204 expected
        """
        response = self.client.post("/teams/create/", 
        {
            "trainer": str(self.trainer_id),
        })
        team_pk = response.json()["id"]

        response = self.client.delete(
            "/teams/get/"+str(team_pk)+"/")
        self.assertEqual(response.status_code, 204)

    def test_delete_team_no_team_exists(self):
        """
        Tries to delete a team that doesn't exist.
        Not Found error expected.
        """
        response = self.client.delete(
            "/teams/get/50000/")
        self.assertEqual(response.status_code, 404)