from django.contrib import admin
from .models import Product, ProductGallery
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'modified_at', 'is_available', 'user')
    prepopulated_fields = {'slug': ('product_name',)}
    readonly_fields = ('user',)
    inlines = [ProductGalleryInline]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
