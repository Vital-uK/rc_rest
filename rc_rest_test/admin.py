from django.contrib import admin
from .models import post, comment

class post_admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'description', 'date')
# Register your models here.
class comment_admin(admin.ModelAdmin):
    list_display = ('id', 'date')

admin.site.register(post, post_admin)
admin.site.register(comment, comment_admin)