from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid
from authentication.utils.user_utils import CreateUserManager


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        app_label = 'authentication'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    owned_guilds = models.IntegerField(default=0)
    member_guilds = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    objects = CreateUserManager()

    def __str__(self):
        return self.email

    
        
        
