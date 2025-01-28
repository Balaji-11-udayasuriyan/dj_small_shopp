from django.contrib import admin
from .models import Category, Brand

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id','name')

    search_fields = ('id','name',)

    ordering = ['id']

admin.site.register(Category,CategoryAdmin)

admin.site.register(Brand)