from django.contrib import admin
from .models import Contact
from . import models

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = 'id', 'first_name', 'last_name','phone', 'show',
  ordering = '-id',
  # list_filter = 'created_date',
  search_fields = 'id', 'first_name', 'last_name',
  list_max_show_all = 200
  list_editable = 'first_name', 'last_name', 'show',
  list_display_links = 'id', 'phone',


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = 'name',
  ordering = '-id',