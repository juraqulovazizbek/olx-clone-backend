from django.db import models
from apps.users.models import User


class SellerProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    shop_name = models.CharField(max_length=250, unique=True)

    shop_description = models.TextField(blank=True)

    shop_logo = models.ImageField(upload_to="shops/", blank=True, null=True)

    region = models.CharField(max_length=100)

    district = models.CharField(max_length=100)

    address = models.CharField(max_length=255, blank=True)

    rating = models.FloatField(default=0)

    total_sales = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shop_name