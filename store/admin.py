from django.contrib import admin

# Register your models here.
from store.models import User, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'slug')
    search_fields = ('brand', 'description')
    prepopulated_fields = {'slug': ('brand', 'model')}
    inlines = [ProductImageInline]
