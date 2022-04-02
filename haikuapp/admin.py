from django.contrib import admin
from .models import Category, Haiku, Comment, Entry_Status, Entry

admin.site.site_header = "WeHaiku Admin"


class CategoryModel(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ("name", "is_deleted")
    list_filter = ['is_deleted', ]


class HaikuModel(admin.ModelAdmin):
    search_fields = ["author", "haiku_status", "title"]
    list_display = ("author", "haiku_status", "title", "is_deleted")
    list_filter = ['is_deleted', 'haiku_status']


class CommentModel(admin.ModelAdmin):
    search_fields = ["name", "comment", "comment_status", "haiku__id"]
    list_display = ("haiku_id", "comment", "comment_status", "rating", "is_deleted")
    list_filter = ['is_deleted', 'comment_status']

    def haiku_id(self, obj):
        return obj.haiku.id
    haiku_id.admin_order_field = 'haiku_id'


class EntryModel(admin.ModelAdmin):
    search_fields = ["haiku_entry", "author_alias"]
    list_display = ("haiku_entry", "author_alias", "haiku_theme", "is_deleted")
    list_filter = ['haiku_theme', 'is_deleted']


admin.site.register(Category, CategoryModel)
admin.site.register(Haiku, HaikuModel)
admin.site.register(Comment, CommentModel)
admin.site.register(Entry_Status)
admin.site.register(Entry, EntryModel)
