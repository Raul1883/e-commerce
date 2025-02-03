from django.db import models
from django.utils.text import slugify


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)  ##Валидация!!!
    email = models.EmailField()


class Product(models.Model):
    class ProductType(models.TextChoices):
        SHOES = 'shoes', 'Обувь'
        CLOTHES = 'clothes', 'Одежда'
        ACCESSORIES = 'accessories', 'Аксессуары'

    description = models.TextField()
    price = models.IntegerField()
    type = models.CharField(
        max_length=255,
        choices=ProductType.choices,
    )
    size = models.CharField(max_length=255)  ##Валидация!!!
    colors = models.CharField(max_length=255)  ##Валидация!!!
    brand = models.CharField(max_length=255)  ##Валидация!!!
    model = models.CharField(max_length=255)  ##Валидация!!!
    image = models.ImageField(upload_to='products/')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.brand} {self.model}")
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()


class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
