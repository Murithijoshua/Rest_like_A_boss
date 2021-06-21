from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Post, Vote


admin.site.register(Vote)
@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'created']
