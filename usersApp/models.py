from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Group, Permission

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Le champ "username" est obligatoire.')
        
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('isAdmin', True)
        return self.create_user(username, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True, blank=False, null=False)
    isAdmin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    groups = models.ManyToManyField(
    Group,
    verbose_name='groups',
    blank=True,
    related_name='user_groups',
    related_query_name='user_group',
    )

    user_permissions = models.ManyToManyField(
    Permission,
    verbose_name='user permissions',
    blank=True,
    related_name='user_permissions',
    related_query_name='user_permission',
    )



    def __str__(self):
         return self.username