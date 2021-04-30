from django.contrib import admin

from .models import CarPost, Comment
# Register your models here.

admin.site.register(CarPost)
admin.site.register(Comment)