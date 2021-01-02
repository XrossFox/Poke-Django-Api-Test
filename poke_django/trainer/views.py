from rest_framework import generics
from trainer.models import Trainer
from trainer.serializers import CreateTrainerSerializer, GetUpdateDestroyTrainerSerializer

# Create your views here.
class TrainerCreate(generics.ListCreateAPIView):
    """
    Generic view for creating a Trainer.
    """
    queryset = Trainer.objects.all()
    serializer_class = CreateTrainerSerializer

class TrainerGetUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic view for getting, updating or destroying a trainer.
    """
    queryset = Trainer.objects.all()
    serializer_class = GetUpdateDestroyTrainerSerializer
