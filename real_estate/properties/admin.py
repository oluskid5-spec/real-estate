from django.contrib import admin
from .models import Category, Property, Inquiry

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "location", "price", "created_at")
    search_fields = ("title", "location", "description")
    list_filter = ("category", "created_at")
    ordering = ("-created_at",)

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "property", "created_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
