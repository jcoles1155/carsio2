from django.contrib import admin

from .models import CarPost, Comment, Photo, UserProfile
# Register your models here.

admin.site.register(CarPost)
admin.site.register(Comment)
admin.site.register(Photo)
admin.site.register(UserProfile)