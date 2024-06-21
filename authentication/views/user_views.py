from rest_framework import generics
from authentication.models.user_models import User
from authentication.serializers.user_serializer import UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class CreateAdminView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class ListUsersView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
   