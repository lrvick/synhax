from django.contrib import admin
from pastebin.models import Snippet
import datetime

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('code','lexer','caption','author','url','email')
    search_fields = ('author', 'lexer', 'caption',)

admin.site.register(Snippet, SnippetAdmin)
