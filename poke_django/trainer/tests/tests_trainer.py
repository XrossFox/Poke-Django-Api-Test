from django.test import TestCase
from rest_framework.test import APIClient
from trainer.models import Trainer

class TrainerTestCase(TestCase):
    """
    Test set for Trainers app.
    """

    def test_create_trainer(self):
        """
        Test case that asserts the user is created properly.
        Must receive a status code 201 and check that the Trainer was created.
        """
        client = APIClient()
        response = client.post('/trainer/create/', {"name":"Roberto", "last_name":"Perez"})
        self.assertEqual(response.status_code, 201)

        trainer = Trainer.objects.get(name="Roberto")
        self.assertEqual(trainer.name, "Roberto")

    def test_create_trainer_bad_data_empty(self):
        """
        Test case that asserts the proper response given wrong json parameters (empty json).
        When empty json is received, default data is used for new trainer.
        """
        client = APIClient()
        response = client.post('/trainer/create/', {})
        self.assertEqual(response.status_code, 201)

        trainer = Trainer.objects.get(name="Red")
        self.assertEqual(trainer.name, "Red")
        self.assertEqual(trainer.last_name, "Oak (lmao)")

        trainer.delete()

    def test_create_trainer_bad_data_wrong_params(self):
        """
        Test case that asserts the proper response given wrong json parameters.
        When wrong parameters are passed
        """
        client = APIClient()
        response = client.post('/trainer/create/', {'neim':'Roberto', 'lasto_neim':'Perez'})
        self.assertEqual(response.status_code, 201)

        trainer = Trainer.objects.get(name="Red")
        self.assertEqual(trainer.name, "Red")
        self.assertEqual(trainer.last_name, "Oak (lmao)")

        trainer.delete()

    def test_delete_trainer(self):
        """
        Test case that asserts the user is deleted properly.
        Must receive a status code 204 and check it no longer exists.
        """
        # create trainer
        client = APIClient()
        response = client.post('/trainer/create/', {"name":"Roberto", "last_name":"Perez"})
        _pk = response.json()["id"]
        self.assertEqual(response.status_code, 201)

        # Delete trainer
        response = client.delete('/trainer/delete/{}/'.format(_pk))
        self.assertEqual(response.status_code, 204)

        # if trainer has been deleted, then when trying
        # to query the db, an excpetion will be raised.
        with self.assertRaises(Exception):
            Trainer.objects.get(name="Roberto")

    def test_delete_trainer_not_exists(self):
        """
        When trying to delete a trainer that doesn't exists, an error 404 must be thrown
        """
        client = APIClient()
        response = client.delete('/trainer/delete/1/')
        self.assertEqual(response.status_code, 404)

    def test_get_trainer(self):
        """
        When requesting via GET a trainer that exists, a json
        with the trainer data must be returned.
        """
        client = APIClient()
        response = client.post('/trainer/create/', {"name":"Roberto", "last_name":"Perez"})
        _pk = response.json()["id"]
        response = client.get('/trainer/get/{}/'.format(_pk))
        self.assertEqual(response.status_code, 200)

        trainer = Trainer.objects.get(name="Roberto")
        self.assertEqual(trainer.name, "Roberto")
        self.assertEqual(trainer.last_name, "Perez")

    def test_get_trainer_not_exists(self):
        """
        When trying to GET a trainer that doesn't exist, a 404 error must be received.
        """
        client = APIClient()
        response = client.get('/trainer/get/5/')
        self.assertEqual(response.status_code, 404)

    def test_update_trainer(self):
        """
        Update a trainer via PUT method, the trainer should be updated
        and a proper response.
        """
        client = APIClient()
        response = client.post('/trainer/create/', {"name":"Roberto", "last_name":"Perez"})
        _pk = response.json()["id"]
        response = client.put('/trainer/update/{}/'.format(_pk),
                                {"name":"Jose", "last_name":"Gonzalez"})
        self.assertEqual(response.status_code, 200)

        trainer = Trainer.objects.get(pk=_pk)
        self.assertEqual(trainer.name, "Jose")
        self.assertEqual(trainer.last_name, "Gonzalez")
        trainer.delete()

    def test_update_trainer_only_name(self):
        """
        Update a trainer via PUT method, the trainer should be updated
        and a proper response.
        """
        client = APIClient()
        response = client.post('/trainer/create/', {"name":"Roberto", "last_name":"Perez"})
        key = response.json()['id']
        response = client.put('/trainer/update/'+str(key)+'/', {"name":"Jose"})
        self.assertEqual(response.status_code, 200)

        trainer = Trainer.objects.get(pk=key)
        self.assertEqual(trainer.name, "Jose")
        self.assertEqual(trainer.last_name, "Perez")
        trainer.delete()

    def test_update_trainer_bad_attribute(self):
        """
        Update a trainer via PUT method, the attributes are wrongly named, so no update
        should be performed.
        """
        client = APIClient()
        response = client.post('/trainer/create/', {"name":"Roberto", "last_name":"Perez"})
        key = response.json()['id']
        response = client.put('/trainer/update/'+str(key)+'/',
        {"neim":"Jose", "lasto_name":"Gonzalez"})
        self.assertEqual(response.status_code, 200)

        trainer = Trainer.objects.get(pk=key)
        self.assertEqual(trainer.name, "Roberto")
        self.assertEqual(trainer.last_name, "Perez")
        trainer.delete()
