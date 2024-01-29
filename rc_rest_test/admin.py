from django.contrib import admin
from .models import rc_rest

# Register your models here.

class rc_rest_admin(admin.ModelAdmin):
    list_display = ('id',  'title', 'description', 'date', 'author', 'comments')
    list_display_links = ('id', 'title', 'comments')
    search_fields = ('id', 'title', 'author')
