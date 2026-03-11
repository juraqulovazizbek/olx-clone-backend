from django.db import models
from apps.sellers.models import SellerProfile
from apps.categories.models import Category


class Product(models.Model):
    class Condition(models.TextChoices):
        NEW = "new", "Yangi"
        USED = "used", "Ishlatilgan"

    class PriceType(models.TextChoices):
        FIXED = "fixed", "Kelishilgan"
        NEGOTIABLE = "negotiable", "Savdolashiladi"

    class Status(models.TextChoices):
        DRAFT = "draft", "Qoralama"
        ACTIVE = "active", "Faol"
        SOLD = "sold", "Sotilgan"
        ARCHIVED = "archived", "Arxiv"

    seller = models.ForeignKey(
        SellerProfile,
        on_delete=models.CASCADE,
        related_name="products"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    price_type = models.CharField(
        max_length=20,
        choices=PriceType.choices,
        default=PriceType.FIXED
    )
    condition = models.CharField(
        max_length=10,
        choices=Condition.choices,
        default=Condition.NEW
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT
    )
    favorite_count = models.PositiveIntegerField(default=0)
    published_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="products/")
    order = models.PositiveIntegerField(default=0)
    is_main = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.product.title}"
    
    