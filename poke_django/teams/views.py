import random
import pokebase as pb
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from teams.models import Team, Pokemon
from teams.serializers import CreateTeamSerializer, GetUpdateDestroyTeamSerializer, PokemonSerializer
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class TeamCreate(generics.ListCreateAPIView):
    """
    Generic view for creating a Trainer.
    """
    queryset = Team.objects.all()
    serializer_class = CreateTeamSerializer

class GetPokemon(generics.RetrieveAPIView):
    """
    Generic view for creating a Trainer.
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

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
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _clear_pokemon_slot(self, model_instance, slot):
        """
        This auxiliary method clears the existing pokemon from the specified slot. If the slot
        is already empty, returns the models as is.
        """
        if str(slot) == "1":
            if model_instance.slot_1_pokemon:
                model_instance.slot_1_pokemon.delete()
                model_instance.slot_1_pokemon = None
            return model_instance

        elif str(slot) == "2":
            if model_instance.slot_2_pokemon:
                model_instance.slot_2_pokemon.delete()
                model_instance.slot_2_pokemon = None
            return model_instance

        elif str(slot) == "3":
            if model_instance.slot_3_pokemon:
                model_instance.slot_3_pokemon.delete()
                model_instance.slot_3_pokemon = None
            return model_instance

        elif str(slot) == "4":
            if model_instance.slot_4_pokemon:
                model_instance.slot_4_pokemon.delete()
                model_instance.slot_4_pokemon = None
            return model_instance

        elif str(slot) == "5":
            if model_instance.slot_5_pokemon:
                model_instance.slot_5_pokemon.delete()
                model_instance.slot_5_pokemon = None
            return model_instance

        elif str(slot) == "6":
            if model_instance.slot_6_pokemon:
                model_instance.slot_6_pokemon.delete()
                model_instance.slot_6_pokemon = None
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
        api_pokemon = pb.pokemon(request.data.get("pokemon_name").lower())

        if not api_pokemon.id_:
            return Response("This pokemon doesn't exist", status=status.HTTP_404_NOT_FOUND)

        try:
            team = self._add_to_slot(team, api_pokemon, request.data.get("slot"))
        except IndexError as _e:
            print(_e)

        team.save()
        serializer = GetUpdateDestroyTeamSerializer(team)
        if serializer.is_valid:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _add_to_slot(self, model_instance, api_pokemon, slot):
        """
        This auxiliary method adds the corresponding pokemon to the correct slot. It requires:
        an instance of the model, an instance of the retrieved pokemon and the slot number
        as a string (as it came straight from the request object). Returns the updated instance
        of the model. If the slot is already filled in, the pokemon will be deleted from db.
        """
        model_pokemon = Pokemon.objects.create(
            team_id=model_instance,
            national_dex_id=api_pokemon.id,
            name=api_pokemon.name,
            species=api_pokemon.species,
            height=api_pokemon.height,
            weight=api_pokemon.weight,
            move_1=random.choice(api_pokemon.moves).move.name,
            move_2=random.choice(api_pokemon.moves).move.name,
            move_3=random.choice(api_pokemon.moves).move.name,
            move_4=random.choice(api_pokemon.moves).move.name
        )
        if len(api_pokemon.types) < 2:
            model_pokemon.type_primary = api_pokemon.types[0].type.name
        else:
            model_pokemon.type_primary = api_pokemon.types[0].type.name
            model_pokemon.type_secondary = api_pokemon.types[1].type.name

        if str(slot) == "1":
            # gotta delete the pokemon if it already exists to avoid orphaned entities
            if model_instance.slot_1_pokemon:
                model_instance.slot_1_pokemon.delete()
            model_pokemon.save()
            model_instance.slot_1_pokemon = model_pokemon
            return model_instance

        if str(slot) == "2":
            # gotta delete the pokemon if it already exists to avoid orphaned entities
            if model_instance.slot_2_pokemon:
                model_instance.slot_2_pokemon.delete()
            model_pokemon.save()
            model_instance.slot_2_pokemon = model_pokemon
            return model_instance

        if str(slot) == "3":
            # gotta delete the pokemon if it already exists to avoid orphaned entities
            if model_instance.slot_3_pokemon:
                model_instance.slot_3_pokemon.delete()
            model_pokemon.save()
            model_instance.slot_3_pokemon = model_pokemon
            return model_instance

        if str(slot) == "4":
            # gotta delete the pokemon if it already exists to avoid orphaned entities
            if model_instance.slot_4_pokemon:
                model_instance.slot_4_pokemon.delete()
            model_pokemon.save()
            model_instance.slot_4_pokemon = model_pokemon
            return model_instance

        if str(slot) == "5":
            # gotta delete the pokemon if it already exists to avoid orphaned entities
            if model_instance.slot_5_pokemon:
                model_instance.slot_5_pokemon.delete()
            model_pokemon.save()
            model_instance.slot_5_pokemon = model_pokemon
            return model_instance

        if str(slot) == "6":
            # gotta delete the pokemon if it already exists to avoid orphaned entities
            if model_instance.slot_6_pokemon:
                model_instance.slot_6_pokemon.delete()
            model_pokemon.save()
            model_instance.slot_6_pokemon = model_pokemon
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
