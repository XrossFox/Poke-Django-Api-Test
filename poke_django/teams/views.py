import random
import pokebase as pb
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

class AddPokemonToTeam(APIView):
    """
    Custom view for adding pokemons to teams.
    """

    def post(self, request):
        """
        Base post method. Adds a new Pokemon from the specified name in the response
        into the team specified in the id. Retrieves the pokemon data from
        PokeApi, its name, size, and four random moves are added (duplicates might occur).
        """
        team = Team.objects.get(pk=request.data.get("id"))
        pokemon = pb.pokemon(request.data.get("pokemon_name").lower())

        if request.data.get("slot") == "1":
            team.slot_1_name = pokemon.name

            if not pokemon.id_:
                return Response("This pokemon doesn't exist", status=status.HTTP_404_NOT_FOUND)

            if len(pokemon.types) < 2:
                team.slot_1_type_primary = pokemon.types[0].type.name
            else:
                team.slot_1_type_primary = pokemon.types[0].type.name
                team.slot_1_type_secondary = pokemon.types[1].type.name
            
            team.slot_1_national_dex_id = pokemon.id
            team.slot_1_type_species = pokemon.species
            team.slot_1_type_height = pokemon.height
            team.slot_1_type_weight = pokemon.weight
            team.slot_1_type_move_1 = random.choice(pokemon.moves).move.name
            team.slot_1_type_move_2 = random.choice(pokemon.moves).move.name
            team.slot_1_type_move_3 = random.choice(pokemon.moves).move.name
            team.slot_1_type_move_4 = random.choice(pokemon.moves).move.name
        
        team.save()
        serializer = GetUpdateDestroyTeamSerializer(team)
        if serializer.is_valid:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
