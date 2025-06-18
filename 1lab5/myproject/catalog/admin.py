from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'sort_order', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active', 'sort_order')
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'description')
        }),
        ('Налаштування', {
            'fields': ('is_active', 'sort_order')
        }),
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'old_price', 'status', 'quantity', 'is_featured', 'is_new', 'created_at')
    list_filter = ('status', 'category', 'is_featured', 'is_new', 'created_at')
    search_fields = ('name', 'description', 'features')
    list_editable = ('price', 'old_price', 'status', 'quantity', 'is_featured', 'is_new')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'category', 'description', 'features')
        }),
        ('Ціна та наявність', {
            'fields': ('price', 'old_price', 'quantity', 'status', 'warranty')
        }),
        ('Позначки', {
            'fields': ('is_featured', 'is_new')
        }),
        ('Додатково', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if obj.quantity <= 0 and obj.status != 'out_of_stock':
            obj.status = 'out_of_stock'
        super().save_model(request, obj, form, change)
