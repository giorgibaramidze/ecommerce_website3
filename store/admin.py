from django.contrib import admin
from .models import Product, ProductGallery, ProductFeature
import admin_thumbnails
from django.utils.html import format_html

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductFeatureInline(admin.StackedInline):
    model = ProductFeature
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('thubnail', 'product_name', 'price', 'stock', 'modified_at', 'is_available', 'created_by')
    prepopulated_fields = {'slug': ('product_name',)}
    readonly_fields = ('created_by',)
    inlines = [ProductGalleryInline, ProductFeatureInline]
    
    def thubnail(self, object):
        return format_html('<img src="{}" width="60" height="60">'.format(object.product_gallery.first()))
    thubnail.short_description = "image"

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
