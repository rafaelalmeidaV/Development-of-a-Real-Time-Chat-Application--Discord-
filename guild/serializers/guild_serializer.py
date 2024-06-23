from rest_framework import serializers
from guild.models.guild_model import Guild
from authentication.serializers.user_serializer import UserSerializer


class GuildSerializer(serializers.ModelSerializer):
    
    id_user_creator = UserSerializer(read_only=True)
    id_user_members = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Guild
        fields = [
            'id',
            'name',
            'description',
            'is_active',
            'id_user_creator',
            'id_user_members'
        ]
        read_only_fields = ['id', 'is_active', 'id_user_creator', 'id_user_members']