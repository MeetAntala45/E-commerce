from django.db import models
from category.models import Category  # Import the Category model from the categories app

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)   # for image python -m pip install Pillow

    def __str__(self):
        return self.name


