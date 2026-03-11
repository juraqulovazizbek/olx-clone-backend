from django.db import models

from apps.users.models import User
from apps.sellers.models import SellerProfile
from apps.products.models import Product


class Order(models.Model):

    class Status(models.TextChoices):
        PENDING = "pending", "Kutilmoqda"
        CONFIRMED = "confirmed", "Tasdiqlangan"
        CANCELLED = "cancelled", "Bekor qilingan"
        COMPLETED = "completed", "Yakunlangan"

    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    seller = models.ForeignKey(
        SellerProfile,
        on_delete=models.CASCADE,
        related_name="sales"
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    total_price = models.DecimalField(max_digits=12, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id}"
    


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    price = models.DecimalField(max_digits=12, decimal_places=2)

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.title} x {self.quantity}"