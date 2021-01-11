from django.contrib import admin
from .models  import Post


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'tags', 'seo_title', 'seo_description')
	prepopulated_fields = {'slug': ('title',), }


admin.site.register(Post, PostAdminj;t )