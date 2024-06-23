import uuid
from django.db import models
from authentication.models.user_models import User


class Guild(models.Model):
    class Meta:
        app_label = 'guild'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    id_user_creator = models.ForeignKey(User, related_name='guildas_criadas', on_delete=models.CASCADE) 
    id_user_members = models.ManyToManyField(User, related_name='guild_members')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
