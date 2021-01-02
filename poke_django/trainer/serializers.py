from rest_framework.serializers import ModelSerializer
from trainer.models import Trainer

class CreateTrainerSerializer(ModelSerializer):
    """
    Model serializer for creating a new trainer.
    """
    class Meta:
        model = Trainer
        fields = ['id', 'name', 'last_name']

class GetUpdateDestroyTrainerSerializer(ModelSerializer):
    """
    Model serializer for GET, PUT and DELETE methods.
    """
    class Meta:
        model = Trainer
        fields = ['id', 'name', 'last_name']
