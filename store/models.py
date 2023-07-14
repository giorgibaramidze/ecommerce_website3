from django.db import models
from django.urls import reverse
from accounts.models import Account
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from category.models import SubCategory, Brand
import uuid
import os

class Product(models.Model):
    created_by = models.ForeignKey(Account, blank=True, null=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(SubCategory, blank=True, null=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.SET_NULL)
    model_pn = models.CharField(max_length=30, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.category.category.slug, self.category.slug, self.slug])

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
        db_table = "product_gallery"

class ProductFeature(models.Model):

    CHOICE_FIELD = [
        ("yes", "Yes"),
        ("no", "No")
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    construction_type= models.CharField(max_length=30, blank=True, null=True)
    type_of_control = models.CharField(max_length=30, blank=True, null=True)
    display = models.CharField(max_length=30, blank=True, null=True)
    engine_type = models.CharField(max_length=30, blank=True, null=True)
    special_features = models.CharField(max_length=30, blank=True, null=True)
    loading_type = models.CharField(max_length=30, blank=True, null=True)

    washing_capacity = models.CharField(max_length=30, blank=True, null=True)
    add_wash = models.CharField(max_length=30, blank=True, null=True, choices=CHOICE_FIELD)
    eco_bubble = models.CharField(max_length=30, blank=True, null=True, choices=CHOICE_FIELD)
    steam_wash = models.CharField(max_length=30, blank=True, null=True, choices=CHOICE_FIELD)

    spin_speed = models.IntegerField(blank=True, null=True)
    speed_adjustment = models.CharField(max_length=30, blank=True, null=True, choices=CHOICE_FIELD)
    water_consumption_per_cycle = models.IntegerField(blank=True, null=True)
    noise_level_wash = models.IntegerField(blank=True, null=True)
    noise_level_spin = models.IntegerField(blank=True, null=True)
     
    color = models.CharField(max_length=30, blank=True, null=True)
    dimensions = models.CharField(max_length=30, blank=True, null=True, help_text="Height x Width x Depth")
    weight =models.IntegerField(blank=True, null=True, help_text="kg")
    varianty_month = models.IntegerField(blank=True, null=True)
    automatic_cold_reservation_hours = models.IntegerField(blank=True, null=True)
    number_of_shelf = models.IntegerField(blank=True, null=True)
    door_pocket = models.IntegerField(blank=True, null=True)
    freezer_location = models.CharField(max_length=30, blank=True, null=True)
    egg_container = models.CharField(max_length=30, blank=True, null=True, choices=CHOICE_FIELD)
    freezer_net_capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "product_feature"