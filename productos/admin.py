from django.contrib import admin
from .models import ProductoT, Favorite
# Register your models here.
# admin.site.register(ProductoT)
@admin.register(ProductoT)
class AdminProducto(admin.ModelAdmin):
	list_display = ('id','name', 'category', 'description', 'price')
	list_filter = ('category',)

@admin.register(Favorite)
class AdminFavorite(admin.ModelAdmin):
	list_display = ('user', 'product',)
	list_filter = ('user', 'product',)
