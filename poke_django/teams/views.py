import random
import pokebase as pb
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from teams.models import Team
from teams.serializers import CreateTeamSerializer, GetUpdateDestroyTeamSerializer
from django.core.exceptions import ObjectDoesNotExist

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

class DeletePokemonFromTeam(APIView):
    """
    Custom view for deleting pokemons from teams.
    """
    def delete(self, request, _pk, slot):
        """
        Delete method. Deletes the pokemon in the specified slot, from the
        specified team by the pk.
        """
        team = None
        try:
            team = Team.objects.get(pk=_pk)
        except ObjectDoesNotExist as _e:
            print(_e)
            return Response("Team not found", status=status.HTTP_404_NOT_FOUND)

        team = self._clear_pokemon_slot(team, slot)
        team.save()

        serializer = GetUpdateDestroyTeamSerializer(team)
        if serializer.is_valid:
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _clear_pokemon_slot(self, model_instance, slot):
        """
        This auxiliary method clears the existing pokemon from the specified slot. If the slot
        is already empty, returns the models as is.
        """
        if str(slot) == "1":
            # none is falsy
            if not model_instance.slot_1_name:
                return model_instance

            model_instance.slot_1_name = None
            model_instance.slot_1_type_primary = None
            model_instance.slot_1_type_secondary = None
            model_instance.slot_1_national_dex_id = None
            model_instance.slot_1_type_species = None
            model_instance.slot_1_type_height = None
            model_instance.slot_1_type_weight = None
            model_instance.slot_1_type_move_1 = None
            model_instance.slot_1_type_move_2 = None
            model_instance.slot_1_type_move_3 = None
            model_instance.slot_1_type_move_4 = None
            return model_instance

        if str(slot) == "2":
            # none is falsy
            if not model_instance.slot_2_name:
                return model_instance

            model_instance.slot_2_name = None
            model_instance.slot_2_type_primary = None
            model_instance.slot_2_type_secondary = None
            model_instance.slot_2_national_dex_id = None
            model_instance.slot_2_type_species = None
            model_instance.slot_2_type_height = None
            model_instance.slot_2_type_weight = None
            model_instance.slot_2_type_move_1 = None
            model_instance.slot_2_type_move_2 = None
            model_instance.slot_2_type_move_3 = None
            model_instance.slot_2_type_move_4 = None
            return model_instance

        if str(slot) == "3":
            # none is falsy
            if not model_instance.slot_3_name:
                return model_instance

            model_instance.slot_3_name = None
            model_instance.slot_3_type_primary = None
            model_instance.slot_3_type_secondary = None
            model_instance.slot_3_national_dex_id = None
            model_instance.slot_3_type_species = None
            model_instance.slot_3_type_height = None
            model_instance.slot_3_type_weight = None
            model_instance.slot_3_type_move_1 = None
            model_instance.slot_3_type_move_2 = None
            model_instance.slot_3_type_move_3 = None
            model_instance.slot_3_type_move_4 = None
            return model_instance

        if str(slot) == "4":
            # none is falsy
            if not model_instance.slot_4_name:
                return model_instance

            model_instance.slot_4_name = None
            model_instance.slot_4_type_primary = None
            model_instance.slot_4_type_secondary = None
            model_instance.slot_4_national_dex_id = None
            model_instance.slot_4_type_species = None
            model_instance.slot_4_type_height = None
            model_instance.slot_4_type_weight = None
            model_instance.slot_4_type_move_1 = None
            model_instance.slot_4_type_move_2 = None
            model_instance.slot_4_type_move_3 = None
            model_instance.slot_4_type_move_4 = None
            return model_instance

        if str(slot) == "5":
            # none is falsy
            if not model_instance.slot_5_name:
                return model_instance

            model_instance.slot_5_name = None
            model_instance.slot_5_type_primary = None
            model_instance.slot_5_type_secondary = None
            model_instance.slot_5_national_dex_id = None
            model_instance.slot_5_type_species = None
            model_instance.slot_5_type_height = None
            model_instance.slot_5_type_weight = None
            model_instance.slot_5_type_move_1 = None
            model_instance.slot_5_type_move_2 = None
            model_instance.slot_5_type_move_3 = None
            model_instance.slot_5_type_move_4 = None
            return model_instance

        if str(slot) == "6":
            # none is falsy
            if not model_instance.slot_6_name:
                return model_instance

            model_instance.slot_6_name = None
            model_instance.slot_6_type_primary = None
            model_instance.slot_6_type_secondary = None
            model_instance.slot_6_national_dex_id = None
            model_instance.slot_6_type_species = None
            model_instance.slot_6_type_height = None
            model_instance.slot_6_type_weight = None
            model_instance.slot_6_type_move_1 = None
            model_instance.slot_6_type_move_2 = None
            model_instance.slot_6_type_move_3 = None
            model_instance.slot_6_type_move_4 = None
            return model_instance

        return model_instance

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
        try:
            team = Team.objects.get(pk=request.data.get("id"))
        except ObjectDoesNotExist as _e:
            print(_e)
            return Response("Team not found", status=status.HTTP_404_NOT_FOUND)
        pokemon = pb.pokemon(request.data.get("pokemon_name").lower())

        if not pokemon.id_:
            return Response("This pokemon doesn't exist", status=status.HTTP_404_NOT_FOUND)

        try:
            team = self._add_to_slot(team, pokemon, request.data.get("slot"))
        except IndexError as _e:
            print(_e)

        team.save()
        serializer = GetUpdateDestroyTeamSerializer(team)
        if serializer.is_valid:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _add_to_slot(self, model_instance, pokemon, slot):
        """
        This auxiliary method adds the corresponding pokemon to the correct slot. It requires:
        an instance of the model, an instance of the retrieved pokemon and the slot number
        as a string (as it came straight from the request object). Returns the updated instance
        of the model.
        """
        if str(slot) == "1":
            model_instance.slot_1_name = pokemon.name

            if len(pokemon.types) < 2:
                model_instance.slot_1_type_primary = pokemon.types[0].type.name
            else:
                model_instance.slot_1_type_primary = pokemon.types[0].type.name
                model_instance.slot_1_type_secondary = pokemon.types[1].type.name

            model_instance.slot_1_national_dex_id = pokemon.id
            model_instance.slot_1_type_species = pokemon.species
            model_instance.slot_1_type_height = pokemon.height
            model_instance.slot_1_type_weight = pokemon.weight
            model_instance.slot_1_type_move_1 = random.choice(pokemon.moves).move.name
            model_instance.slot_1_type_move_2 = random.choice(pokemon.moves).move.name
            model_instance.slot_1_type_move_3 = random.choice(pokemon.moves).move.name
            model_instance.slot_1_type_move_4 = random.choice(pokemon.moves).move.name
            return model_instance

        if str(slot) == "2":
            model_instance.slot_2_name = pokemon.name

            if len(pokemon.types) < 2:
                model_instance.slot_2_type_primary = pokemon.types[0].type.name
            else:
                model_instance.slot_2_type_primary = pokemon.types[0].type.name
                model_instance.slot_2_type_secondary = pokemon.types[1].type.name

            model_instance.slot_2_national_dex_id = pokemon.id
            model_instance.slot_2_type_species = pokemon.species
            model_instance.slot_2_type_height = pokemon.height
            model_instance.slot_2_type_weight = pokemon.weight
            model_instance.slot_2_type_move_1 = random.choice(pokemon.moves).move.name
            model_instance.slot_2_type_move_2 = random.choice(pokemon.moves).move.name
            model_instance.slot_2_type_move_3 = random.choice(pokemon.moves).move.name
            model_instance.slot_2_type_move_4 = random.choice(pokemon.moves).move.name
            return model_instance

        if str(slot) == "3":
            model_instance.slot_3_name = pokemon.name

            if len(pokemon.types) < 2:
                model_instance.slot_3_type_primary = pokemon.types[0].type.name
            else:
                model_instance.slot_3_type_primary = pokemon.types[0].type.name
                model_instance.slot_3_type_secondary = pokemon.types[1].type.name

            model_instance.slot_3_national_dex_id = pokemon.id
            model_instance.slot_3_type_species = pokemon.species
            model_instance.slot_3_type_height = pokemon.height
            model_instance.slot_3_type_weight = pokemon.weight
            model_instance.slot_3_type_move_1 = random.choice(pokemon.moves).move.name
            model_instance.slot_3_type_move_2 = random.choice(pokemon.moves).move.name
            model_instance.slot_3_type_move_3 = random.choice(pokemon.moves).move.name
            model_instance.slot_3_type_move_4 = random.choice(pokemon.moves).move.name
            return model_instance

        if str(slot) == "4":
            model_instance.slot_4_name = pokemon.name

            if len(pokemon.types) < 2:
                model_instance.slot_4_type_primary = pokemon.types[0].type.name
            else:
                model_instance.slot_4_type_primary = pokemon.types[0].type.name
                model_instance.slot_4_type_secondary = pokemon.types[1].type.name

            model_instance.slot_4_national_dex_id = pokemon.id
            model_instance.slot_4_type_species = pokemon.species
            model_instance.slot_4_type_height = pokemon.height
            model_instance.slot_4_type_weight = pokemon.weight
            model_instance.slot_4_type_move_1 = random.choice(pokemon.moves).move.name
            model_instance.slot_4_type_move_2 = random.choice(pokemon.moves).move.name
            model_instance.slot_4_type_move_3 = random.choice(pokemon.moves).move.name
            model_instance.slot_4_type_move_4 = random.choice(pokemon.moves).move.name
            return model_instance

        if str(slot) == "5":
            model_instance.slot_5_name = pokemon.name

            if len(pokemon.types) < 2:
                model_instance.slot_5_type_primary = pokemon.types[0].type.name
            else:
                model_instance.slot_5_type_primary = pokemon.types[0].type.name
                model_instance.slot_5_type_secondary = pokemon.types[1].type.name

            model_instance.slot_5_national_dex_id = pokemon.id
            model_instance.slot_5_type_species = pokemon.species
            model_instance.slot_5_type_height = pokemon.height
            model_instance.slot_5_type_weight = pokemon.weight
            model_instance.slot_5_type_move_1 = random.choice(pokemon.moves).move.name
            model_instance.slot_5_type_move_2 = random.choice(pokemon.moves).move.name
            model_instance.slot_5_type_move_3 = random.choice(pokemon.moves).move.name
            model_instance.slot_5_type_move_4 = random.choice(pokemon.moves).move.name
            return model_instance

        if str(slot) == "6":
            model_instance.slot_6_name = pokemon.name

            if len(pokemon.types) < 2:
                model_instance.slot_6_type_primary = pokemon.types[0].type.name
            else:
                model_instance.slot_6_type_primary = pokemon.types[0].type.name
                model_instance.slot_6_type_secondary = pokemon.types[1].type.name

            model_instance.slot_6_national_dex_id = pokemon.id
            model_instance.slot_6_type_species = pokemon.species
            model_instance.slot_6_type_height = pokemon.height
            model_instance.slot_6_type_weight = pokemon.weight
            model_instance.slot_6_type_move_1 = random.choice(pokemon.moves).move.name
            model_instance.slot_6_type_move_2 = random.choice(pokemon.moves).move.name
            model_instance.slot_6_type_move_3 = random.choice(pokemon.moves).move.name
            model_instance.slot_6_type_move_4 = random.choice(pokemon.moves).move.name
            return model_instance

        raise IndexError("Slot can only be between 1 and 6")

class GetallTeams(APIView):
    """
    APIView for getall endpoint. Returns all teams belonging to a given trainer.
    """

    def get(self, request, _id):
        """
        GET Method returns all teams belonging to specified trainer by id.
        """
        teams = Team.objects.filter(trainer=_id)

        if not teams:
            return Response({"message": "No teams found"}, status=status.HTTP_204_NO_CONTENT)

        serializer = GetUpdateDestroyTeamSerializer(teams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
