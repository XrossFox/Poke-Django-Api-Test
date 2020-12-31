from rest_framework.serializers import ModelSerializer
from teams.models import Team

class CreateTeamSerializer(ModelSerializer):
    """
    Serializer when a Team is created
    """
    class Meta:
        model = Team
        fields = ['id',
        'trainer',]

class GetUpdateDestroyTeamSerializer(ModelSerializer):
    """
    Serializer for everything else #YOLO
    """
    class Meta:
        model = Team
        fields = [
        'id',
        'trainer',
        'slot_1_national_dex_id',
        'slot_1_name',
        'slot_1_type_primary',
        'slot_1_type_secondary',
        'slot_1_type_species',
        'slot_1_type_height',
        'slot_1_type_weight',
        'slot_1_type_move_1',
        'slot_1_type_move_2',
        'slot_1_type_move_3',
        'slot_1_type_move_4',
        'slot_2_national_dex_id',
        'slot_2_name',
        'slot_2_type_primary',
        'slot_2_type_secondary',
        'slot_2_type_species',
        'slot_2_type_height',
        'slot_2_type_weight',
        'slot_2_type_move_1',
        'slot_2_type_move_2',
        'slot_2_type_move_3',
        'slot_2_type_move_4',
        'slot_3_national_dex_id',
        'slot_3_name',
        'slot_3_type_primary',
        'slot_3_type_secondary',
        'slot_3_type_species',
        'slot_3_type_height',
        'slot_3_type_weight',
        'slot_3_type_move_1',
        'slot_3_type_move_2',
        'slot_3_type_move_3',
        'slot_3_type_move_4',
        'slot_4_national_dex_id',
        'slot_4_name',
        'slot_4_type_primary',
        'slot_4_type_secondary',
        'slot_4_type_species',
        'slot_4_type_height',
        'slot_4_type_weight',
        'slot_4_type_move_1',
        'slot_4_type_move_2',
        'slot_4_type_move_3',
        'slot_4_type_move_4',
        'slot_5_national_dex_id',
        'slot_5_name',
        'slot_5_type_primary',
        'slot_5_type_secondary',
        'slot_5_type_species',
        'slot_5_type_height',
        'slot_5_type_weight',
        'slot_5_type_move_1',
        'slot_5_type_move_2',
        'slot_5_type_move_3',
        'slot_5_type_move_4',
        'slot_6_national_dex_id',
        'slot_6_name',
        'slot_6_type_primary',
        'slot_6_type_secondary',
        'slot_6_type_species',
        'slot_6_type_height',
        'slot_6_type_weight',
        'slot_6_type_move_1',
        'slot_6_type_move_2',
        'slot_6_type_move_3',
        'slot_6_type_move_4',
        ]
