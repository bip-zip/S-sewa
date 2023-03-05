from django.contrib import admin
from .models import  Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin): 
    list_display=('id', 'title', 'publish','slug')
    list_display_links=('id','title',)
    search_fields=('title',)
    list_per_page =25
    summernote_fields = ('body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')