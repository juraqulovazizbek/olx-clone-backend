from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=150, unique=True)

    slug = models.SlugField(unique=True)

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children"
    )

    icon = models.ImageField(upload_to="categories/", blank=True, null=True)

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    order_num = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name