from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .mangers import CustomUserManager

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
    
class AttackProfile(models.Model):
    # offensive modifiers
	attacks = models.IntegerField(default=12)
	clash = models.IntegerField(default=2)
	reroll = models.BooleanField(default=False)
	rr6s = models.BooleanField(default=False)
	relentless = models.BooleanField(default=False)
	torrential = models.BooleanField(default=False)
	rr1s = models.BooleanField(default=False)

	# Defenesive modifiers
	defence = models.IntegerField(default=2)
	cleave = models.IntegerField(default=0)
	hardened = models.IntegerField(default=0)
	evasion = models.IntegerField(default=0)
	deadly = models.BooleanField(default=False)
	precice = models.BooleanField(default=False)
	defRR = models.BooleanField(default=False)
	rr6def = models.BooleanField(default=False)
	rr1def = models.BooleanField(default=False)
	shield = models.BooleanField(default=False)
	lineBreaker = models.BooleanField(default=False)
	smite = models.BooleanField(default=False)
	tenacious = models.IntegerField(default=0)
	bastion = models.IntegerField(default=0)

	# Morale Modifiers
	ignoresResolves = models.BooleanField(default=False)
	resolve = models.IntegerField(default=3)
	terrifying = models.IntegerField(default=0)
	fearless = models.BooleanField(default=False)
	indomitable = models.IntegerField(default=0)
	rrSuccess = models.BooleanField(default=False)
	rrResolve = models.BooleanField(default=False)
	rr6Res = models.BooleanField(default=False)
	rr1Res = models.BooleanField(default=False)
	oblivious = models.BooleanField(default=False)
    
	def __str__(self):
		"""Returns all the values of the entered Profiles."""
		return [self.attacks, self.clash, self.reroll, self.rr6s, self.relentless, self.torrential, self.rr1s, self.defence, self.cleave, self.hardened, self.evasion, self.deadly, self.precice, self.defRR, self.rr6def, self.rr1def, self.shield, self.lineBreaker, self.smite, self.tenacious, self.bastion, self.ignoresResolves, self.resolve, self.terrifying, self.fearless, self.indomitable, self.rrSuccess, self.rrResolve, self.rr6Res, self.rr1Res, self.oblivious]

# class CustomUser(AbstractUser):
#     username = None
#     first_name = None
#     last_name = None
#     is_staff = None
#     is_superuser = None
#     email = models.EmailField(_("email address"), unique=True)
#     savedProfiles = models.ForeignKey(
#         "Profiles",
#         on_delete=models.CASCADE,
#     )

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email
    
# class unitProfile():
#     pass