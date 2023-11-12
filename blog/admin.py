from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin #관리자 페이지 마크다운
from .models import Post, Category, Tag

admin.site.register(Post, MarkdownxModelAdmin) #관리자 페이지 마크다운

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
