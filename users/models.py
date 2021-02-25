from datetime import date
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False,
                    is_active=True, name='', **extra_fields):
        email = UserManager.normalize_email(email)
        user = self.model(email=email, is_active=is_active,
                          is_staff=is_staff, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(email, password, is_staff=True,
                                is_superuser=True, **extra_fields)


"""Override and extend the default django user model"""
class User(PermissionsMixin, AbstractBaseUser):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=True)
    is_customer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    send_mail = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, null=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return f"id={self.id}, name={self.name}, email={self.email}, is_staff={self.is_staff}, is_customer={self.is_customer}, is_active={self.is_active}, send_mail={self.send_mail}"
