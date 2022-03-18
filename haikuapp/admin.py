from django.contrib import admin
from .models import Category, Haiku, Comment, Entry_Status, Entry

admin.site.site_header = "WeHaiku Admin"

admin.site.register(Category)
admin.site.register(Haiku)
admin.site.register(Comment)
admin.site.register(Entry_Status)
admin.site.register(Entry)
