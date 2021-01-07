from django.contrib import admin
from myApp.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    l = ['title', 'slug', 'author', 'body', 'publish', 'created', 'updated', 'status']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    ordering = ['status', 'publish']
    raw_id_fields = ('author',)
admin.site.register(Post,PostAdmin)
