from rest_framework.serializers import ModelSerializer
from trainer.models import Trainer

class CreateTrainerSerializer(ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['id', 'name', 'last_name']

class GetUpdateDestroyTrainerSerializer(ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['id', 'name', 'last_name']