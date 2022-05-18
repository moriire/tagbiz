from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
from django.core.validators import RegexValidator

class CustomUser(AbstractBaseUser, PermissionsMixin):
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    auth_code = models.CharField(null=True, blank=True, max_length = 30)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    objects = CustomUserManager()


    def get_full_name(self):
        # The user is identified by their email address
        return f"{self.first_name} {self.last_name}"

    def get_username(self):
        return self.email.split("@")[0]

    def get_email(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email
