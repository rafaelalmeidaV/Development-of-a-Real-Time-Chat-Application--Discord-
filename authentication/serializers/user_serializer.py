from rest_framework import serializers
from authentication.models.user_models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'username',
            'email',
            'password',
            'is_active',
            'is_admin',
            'is_staff',
            'owned_guilds',
            'member_guilds'
        ]
        read_only_fields = [
            'is_active',
            'is_admin',
            'is_staff',
            'owned_guilds'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class ADMSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'is_active', 'is_admin', 'is_staff']
        read_only_fields = ['is_active', 'is_admin', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_admin = True
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
