from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from guild.models.guild_model import Guild
from guild.serializers.guild_serializer import GuildSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from authentication.models.user_models import User
from authentication.serializers.user_serializer import UserSerializer

class AddMemberToGuild(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, guild_id, user_id):
        guild = get_object_or_404(Guild, id=guild_id)
        if request.user != guild.id_user_creator:
            return Response({"message": "Apenas o criador pode adicionar membros."}, status=status.HTTP_403_FORBIDDEN)
        
        user = get_object_or_404(User, id=user_id)
        guild.id_user_members.add(user)
        guild.save()
        
        user_data = UserSerializer(user).data
        return Response({"message": "Membro adicionado com sucesso."}, status=status.HTTP_200_OK)


class CreateListGuild(generics.ListCreateAPIView):
    serializer_class = GuildSerializer
    permission_classes = [IsAuthenticated]
    queryset = Guild.objects.all()

    def perform_create(self, serializer):
        serializer.save(id_user_creator=self.request.user)
    
    
        
class RetrieveUpdateDeleteGuild(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GuildSerializer
    permission_classes = (IsAuthenticated)
    queryset = Guild.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def destroy(self):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)