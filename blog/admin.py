from django.contrib import admin
from .models import Post, Category, Comment

#Adding admin priviledges to add/delete/update posts, comments and categories
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)