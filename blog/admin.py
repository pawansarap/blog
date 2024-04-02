from django.contrib import admin
from blog.models import Contact
from .models import Blog
# Register your models here.
admin.site.register(Contact),
admin.site.register(Blog)
# @admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'datetime')
    