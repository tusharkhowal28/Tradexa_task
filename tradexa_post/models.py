from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
import datetime
from django.utils import timezone

# Create your models here.

class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    username = models.CharField(max_length=32, unique=True,)
    email = models.EmailField(max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return str(self.email) 


class Post(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField(max_length = 500)
    author = models.ForeignKey(
       to=CustomUser,
        on_delete=models.CASCADE,
        related_name="post_author"
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    thumbnail = models.ImageField(
        upload_to="User_post", null=True, default=None, blank=True)
    def __str__(self):
        return self.title + " by " + str(self.author.first_name)

