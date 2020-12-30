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
        fields = ['id',
        'trainer',
        'slot_1_dex_id',
        'slot_1_name',
        'slot_2_dex_id',
        'slot_2_name',
        'slot_3_dex_id',
        'slot_3_name',
        'slot_4_dex_id',
        'slot_4_name',
        'slot_5_dex_id',
        'slot_5_name',
        'slot_6_dex_id',
        'slot_6_name',]
