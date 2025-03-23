# blog/admin.py
from django.contrib import admin
from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_filter = ('is_published', )
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_filter = ('is_published', )
    search_fields = ('name', )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author', 'category', 'is_published')
    list_filter = ('is_published', 'category', 'author')
    search_fields = ('title', 'text')
    date_hierarchy = 'pub_date'
    readonly_fields = ('created_at',)

