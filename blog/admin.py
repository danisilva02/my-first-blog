from django.contrib import admin

# Register your models here.
from blog.models import Category, Post_home, banner, Video

class PostAdmin(admin.ModelAdmin):
      list_display = ('name', 'status', 'category')
      search_fields = ['id', 'name', 'content']
      list_filter = ['status', 'category', 'created_at']

admin.site.register(Category)
admin.site.register(Post_home, PostAdmin)
admin.site.register(banner)
admin.site.register(Video)