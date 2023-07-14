from django.db import models
from django.urls import reverse
from accounts.models import Account

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='categories', null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        db_table = 'category'

    def get_absolute_url(self):
        return reverse('products_by_category', args=[self.slug])

    
    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    sub_category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sub_category'
        verbose_name = 'sub category'
        verbose_name_plural = 'Sub Categories'

    def __str__(self):
        return self.sub_category_name
    
class Brand(models.Model):
    created_by = models.ForeignKey(Account, blank=True, null=True, on_delete=models.SET_NULL)
    brand_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.brand_name
