from django.contrib.auth.models import BaseUserManager



class CreateUserManager(BaseUserManager):
    def create_user(self, email, username, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not name:
            raise ValueError('Users must have a name')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, password):
        user = self.create_user(
            email,
            username=username,
            name=name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user