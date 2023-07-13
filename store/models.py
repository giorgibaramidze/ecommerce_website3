from django.db import models
from django.urls import reverse
from accounts.models import Account
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from category.models import SubCategory
import uuid
import os

class Product(models.Model):
    user = models.ForeignKey(Account, blank=True, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(SubCategory, blank=True, null=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def __str__(self):
        return self.product_name
    

    class Meta:
        ordering = ['-modified_at']
        db_table = 'product'


class ProductGallery(models.Model):

    def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('products', filename)

    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE, related_name='product_gallery')
    image = models.ImageField(upload_to=get_file_path)

    def __str__(self):
        return self.image.url
    
    class Meta:
        verbose_name = 'Product Gallery'
        verbose_name_plural = "Product Gallery"
