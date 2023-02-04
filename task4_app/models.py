from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
import uuid

class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default="")


    def __str__(self):
        return self.name 


class UserManager(BaseUserManager):
    def create_superuser(self, **kwargs):
        user = self.model(email=kwargs["email"])
        user.set_password(kwargs["password"])
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):

    class RoleTypes(models.TextChoices):
        admin = "admin"
        manager = "manager"
        staff = "staff"

    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=RoleTypes.choices,default="")
    group_name = models.ForeignKey(Group, related_name="group_name", on_delete=models.CASCADE, null=True, blank=True)

    objects = UserManager()


    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.fullname
