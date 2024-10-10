from django.contrib import admin
from .models import Business

# Register your models here.
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('social_name', 'nif', 'is_active', 'created_at', 'updated_at')
    search_fields = ('social_name', 'nif')
    list_filter = ('is_active',)

admin.site.register(Business, BusinessAdmin)
