from django.contrib import admin

# Register your models here.
from .models import Photo

# for the custom display use ModelAdmin
class PhotoAdmin(admin.ModelAdmin):
    # display columns
    list_display = ['id', 'author', 'created', 'updated']
    # search for author instead of list
    raw_id_fields = ['author']
    # enable filter
    list_filter = ['created', 'updated', 'author']
    # you can search these fields
    search_fields = ['text', 'created', 'author__username']
    # ordering '-' meaning descending order
    ordering = ['-updated', '-created']

admin.site.register(Photo, PhotoAdmin)