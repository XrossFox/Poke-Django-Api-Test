from rest_framework.serializers import ModelSerializer
from teams.models import Team, Pokemon

class CreateTeamSerializer(ModelSerializer):
    """
    Serializer when a Team is created
    """
    class Meta:
        model = Team
        fields = ['id',
        'trainer',]

class PokemonSerializer(ModelSerializer):
    """
    Serializer for Pokemon model representation.
    """
    class Meta:
        model = Pokemon
        fields = [
            "team_id",
            "national_dex_id",
            "name",
            "type_primary",
            "type_secondary",
            "species",
            "height",
            "weight",
            "move_1",
            "move_2",
            "move_3",
            "move_4",
        ]

class GetUpdateDestroyTeamSerializer(ModelSerializer):
    """
    Serializer for everything else #YOLO
    """
    slot_1_pokemon = PokemonSerializer(read_only=True)
    slot_2_pokemon = PokemonSerializer(read_only=True)
    slot_3_pokemon = PokemonSerializer(read_only=True)
    slot_4_pokemon = PokemonSerializer(read_only=True)
    slot_5_pokemon = PokemonSerializer(read_only=True)
    slot_6_pokemon = PokemonSerializer(read_only=True)

    class Meta:
        model = Team
        fields = [
        'id',
        'trainer',
        'slot_1_pokemon',
        'slot_2_pokemon',
        'slot_3_pokemon',
        'slot_4_pokemon',
        'slot_5_pokemon',
        'slot_6_pokemon',
        ]
