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

        if not pokemon.id_:
            return Response("This pokemon doesn't exist", status=status.HTTP_404_NOT_FOUND)

        team = self._add_to_slot(team, pokemon, request.data.get("slot"))

        team.save()
        serializer = GetUpdateDestroyTeamSerializer(team)
        if serializer.is_valid:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _add_to_slot(self, modelInstance, pokemon, slot):
        """
        This auxiliary method adds the corresponding pokemon to the correct slot. It requires:
        an instance of the model, an instance of the retrieved pokemon and the slot number
        as a string (as it came straight from the request object). Returns the updated instance
        of the model.
        """
        if str(slot) == "1":
            modelInstance.slot_1_name = pokemon.name

            if len(pokemon.types) < 2:
                modelInstance.slot_1_type_primary = pokemon.types[0].type.name
            else:
                modelInstance.slot_1_type_primary = pokemon.types[0].type.name
                modelInstance.slot_1_type_secondary = pokemon.types[1].type.name

            modelInstance.slot_1_national_dex_id = pokemon.id
            modelInstance.slot_1_type_species = pokemon.species
            modelInstance.slot_1_type_height = pokemon.height
            modelInstance.slot_1_type_weight = pokemon.weight
            modelInstance.slot_1_type_move_1 = random.choice(pokemon.moves).move.name
            modelInstance.slot_1_type_move_2 = random.choice(pokemon.moves).move.name
            modelInstance.slot_1_type_move_3 = random.choice(pokemon.moves).move.name
            modelInstance.slot_1_type_move_4 = random.choice(pokemon.moves).move.name
            return modelInstance
        
        elif str(slot) == "2":
            modelInstance.slot_2_name = pokemon.name

            if len(pokemon.types) < 2:
                modelInstance.slot_2_type_primary = pokemon.types[0].type.name
            else:
                modelInstance.slot_2_type_primary = pokemon.types[0].type.name
                modelInstance.slot_2_type_secondary = pokemon.types[1].type.name

            modelInstance.slot_2_national_dex_id = pokemon.id
            modelInstance.slot_2_type_species = pokemon.species
            modelInstance.slot_2_type_height = pokemon.height
            modelInstance.slot_2_type_weight = pokemon.weight
            modelInstance.slot_2_type_move_1 = random.choice(pokemon.moves).move.name
            modelInstance.slot_2_type_move_2 = random.choice(pokemon.moves).move.name
            modelInstance.slot_2_type_move_3 = random.choice(pokemon.moves).move.name
            modelInstance.slot_2_type_move_4 = random.choice(pokemon.moves).move.name
            return modelInstance

        elif str(slot) == "3":
            modelInstance.slot_3_name = pokemon.name

            if len(pokemon.types) < 2:
                modelInstance.slot_3_type_primary = pokemon.types[0].type.name
            else:
                modelInstance.slot_3_type_primary = pokemon.types[0].type.name
                modelInstance.slot_3_type_secondary = pokemon.types[1].type.name

            modelInstance.slot_3_national_dex_id = pokemon.id
            modelInstance.slot_3_type_species = pokemon.species
            modelInstance.slot_3_type_height = pokemon.height
            modelInstance.slot_3_type_weight = pokemon.weight
            modelInstance.slot_3_type_move_1 = random.choice(pokemon.moves).move.name
            modelInstance.slot_3_type_move_2 = random.choice(pokemon.moves).move.name
            modelInstance.slot_3_type_move_3 = random.choice(pokemon.moves).move.name
            modelInstance.slot_3_type_move_4 = random.choice(pokemon.moves).move.name
            return modelInstance

        elif str(slot) == "4":
            modelInstance.slot_4_name = pokemon.name

            if len(pokemon.types) < 2:
                modelInstance.slot_4_type_primary = pokemon.types[0].type.name
            else:
                modelInstance.slot_4_type_primary = pokemon.types[0].type.name
                modelInstance.slot_4_type_secondary = pokemon.types[1].type.name

            modelInstance.slot_4_national_dex_id = pokemon.id
            modelInstance.slot_4_type_species = pokemon.species
            modelInstance.slot_4_type_height = pokemon.height
            modelInstance.slot_4_type_weight = pokemon.weight
            modelInstance.slot_4_type_move_1 = random.choice(pokemon.moves).move.name
            modelInstance.slot_4_type_move_2 = random.choice(pokemon.moves).move.name
            modelInstance.slot_4_type_move_3 = random.choice(pokemon.moves).move.name
            modelInstance.slot_4_type_move_4 = random.choice(pokemon.moves).move.name
            return modelInstance

        elif str(slot) == "5":
            modelInstance.slot_5_name = pokemon.name

            if len(pokemon.types) < 2:
                modelInstance.slot_5_type_primary = pokemon.types[0].type.name
            else:
                modelInstance.slot_5_type_primary = pokemon.types[0].type.name
                modelInstance.slot_5_type_secondary = pokemon.types[1].type.name

            modelInstance.slot_5_national_dex_id = pokemon.id
            modelInstance.slot_5_type_species = pokemon.species
            modelInstance.slot_5_type_height = pokemon.height
            modelInstance.slot_5_type_weight = pokemon.weight
            modelInstance.slot_5_type_move_1 = random.choice(pokemon.moves).move.name
            modelInstance.slot_5_type_move_2 = random.choice(pokemon.moves).move.name
            modelInstance.slot_5_type_move_3 = random.choice(pokemon.moves).move.name
            modelInstance.slot_5_type_move_4 = random.choice(pokemon.moves).move.name
            return modelInstance

        elif str(slot) == "6":
            modelInstance.slot_6_name = pokemon.name

            if len(pokemon.types) < 2:
                modelInstance.slot_6_type_primary = pokemon.types[0].type.name
            else:
                modelInstance.slot_6_type_primary = pokemon.types[0].type.name
                modelInstance.slot_6_type_secondary = pokemon.types[1].type.name

            modelInstance.slot_6_national_dex_id = pokemon.id
            modelInstance.slot_6_type_species = pokemon.species
            modelInstance.slot_6_type_height = pokemon.height
            modelInstance.slot_6_type_weight = pokemon.weight
            modelInstance.slot_6_type_move_1 = random.choice(pokemon.moves).move.name
            modelInstance.slot_6_type_move_2 = random.choice(pokemon.moves).move.name
            modelInstance.slot_6_type_move_3 = random.choice(pokemon.moves).move.name
            modelInstance.slot_6_type_move_4 = random.choice(pokemon.moves).move.name
            return modelInstance

        else:
            raise Exception("Check your slot, pal")
