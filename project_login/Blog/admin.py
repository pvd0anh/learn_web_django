from django.contrib import admin
from Blog.models import Blog


class Blog_admin(admin.ModelAdmin):
    list_display = ('name', 'topic', 'viewer')
    search_fields = ('name',)


# Register your models here.
admin.site.register(Blog, Blog_admin)
