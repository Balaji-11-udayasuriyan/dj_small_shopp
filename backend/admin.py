from django.contrib import admin
from .models import Category, Brand

# Register your models here.

# categroy admin

class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id','name')

    search_fields = ('id','name',)

    ordering = ['id']

admin.site.register(Category,CategoryAdmin)

# brand admin

class BrandAdmin(admin.ModelAdmin):

    list_display = ('id','name','image_path','status',)

    search_fields = ('id','name','status')

    ordering = ['id']

admin.site.register(Brand,BrandAdmin)