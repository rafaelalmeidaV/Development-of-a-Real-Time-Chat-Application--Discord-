from rest_framework import generics
from authentication.models.user_models import User
from authentication.serializers.user_serializer import UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.db.models import Count
from rest_framework.response import Response
from rest_framework import status
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class CreateAdminView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    

class ListUserbyEmailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    filterset_fields = ["email"]
    pagination_class = None 
    
    def list(self, request):
        email = request.query_params.get('email', None)
        if email is not None:
            queryset = User.objects.filter(email=email)
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "Email não informado"}, status=status.HTTP_400_BAD_REQUEST)
    

class ListUsersView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def get_queryset(self):
        queryset = User.objects.all()
        name = self.request.query_params.get('name', None)
        email = self.request.query_params.get('email', None)
        id = self.request.query_params.get('id', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        if email is not None:
            queryset = queryset.filter(email=email)
        if id is not None:
            queryset = queryset.filter(id=id) 
        
        
        return queryset
   