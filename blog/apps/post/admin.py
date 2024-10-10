from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'date', 'text', 'active', 'category', 'image', 'published')

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
