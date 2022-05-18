from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, phone, gender, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
    
        if not email:
            raise ValueError(_('The Email must be set'))
        elif not phone:
            raise ValueError(_('Phone number must be set'))
        elif not gender:
            raise ValueError(_('Sex must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, gender=gender, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, gender, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, phone, gender, **extra_fields)
    
