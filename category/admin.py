from django.contrib import admin
from .models import Category, SubCategory

class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1
    prepopulated_fields = {'slug': ('sub_category_name',)}
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'modified_at', 'created_at')
    prepopulated_fields = {'slug': ('category_name',)}
    inlines = [SubCategoryInline]

# @admin.register(SubCategory)
# class SubCategoryAdmin(admin.ModelAdmin):
#     list_display = ('category', 'sub_category_name', 'modified_at', 'created_at')
#     prepopulated_fields = {'slug': ('sub_category_name',)}

# Register your models here.
