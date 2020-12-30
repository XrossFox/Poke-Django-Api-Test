from rest_framework import generics
from teams.models import Team
from teams.serializers import CreateTeamSerializer, GetUpdateDestroyTeamSerializer

# Create your views here.
class TeamCreate(generics.ListCreateAPIView):
    """
    Generic view for creating a Trainer.
    """
    queryset = Team.objects.all()
    serializer_class = CreateTeamSerializer

class TeamGetUpdateDestroy(generics.RetrieveDestroyAPIView):
    """
    Generic view for getting, updating or destroying a trainer.
    """
    queryset = Team.objects.all()
    serializer_class = GetUpdateDestroyTeamSerializer
