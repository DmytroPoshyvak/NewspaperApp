from django.db import models
from django.contrib.auth.models import AbstractUser

class PersonalCustomUser(AbstractUser):
    age = models.PositiveBigIntegerField(blank=True , null=True)
    email  = models.EmailField(blank=True , null=True)
