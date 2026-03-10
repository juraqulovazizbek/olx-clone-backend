from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        CUSTOMER = "customer", "Xaridor"
        SELLER = "seller", "Sotuvchi"

    telegram_id = models.BigIntegerField(unique=True)

    username = models.CharField( max_length=150, unique=True)

    first_name = models.CharField(max_length=150)

    last_name = models.CharField(max_length=150, blank=True)	

    phone_number = models.CharField(max_length=20, blank=True)

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.CUSTOMER
    )

    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(Default=True)

    date_joined	= models.DateTimeField(auto_now_add=True)

    last_login = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.username