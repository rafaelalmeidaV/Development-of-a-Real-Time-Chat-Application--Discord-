from rest_framework import serializers
from guild.models.guild_model import Guild


class GuildSerializer(serializers.ModelSerializer):
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