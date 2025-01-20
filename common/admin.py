from django.contrib import admin

from common.models import Author, BlogPost

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Author)
