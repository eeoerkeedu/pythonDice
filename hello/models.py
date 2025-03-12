from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .mangers import CustomUserManager

# class LogMessage(models.Model):
#     message = models.CharField(max_length=300)
#     log_date = models.DateTimeField("date logged")

#     def __str__(self):
#         """Returns a string representation of a message."""
#         date = timezone.localtime(self.log_date)
#         return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

class CustomUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    is_staff = None
    is_superuser = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email