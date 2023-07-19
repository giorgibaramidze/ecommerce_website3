from django.contrib import admin
from .models import Category, SubCategory, Brand

class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1
    prepopulated_fields = {'slug': ('sub_category_name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'modified_at', 'created_at')
    prepopulated_fields = {'slug': ('category_name',)}
    inlines = [SubCategoryInline]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'created_by', 'get_category')
    readonly_fields = ('created_by',)

    def get_category(self, obj):
        return ", ".join([c.sub_category_name for c in obj.sub_category.all()])

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'sub_category_name', 'modified_at', 'created_at')
    prepopulated_fields = {'slug': ('sub_category_name',)}
