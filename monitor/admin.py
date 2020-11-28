from django.contrib import admin
from .models import Source, Stat
from django.utils.html import format_html


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):

    def thumb(self, obj):
        return format_html('<img src="{}" width="30" height="30" />'.format(obj.avatar))

    list_display = 'thumb', 'name', 'link', 'internal_id', 'type_social'
    list_display_links = 'name',


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = 'id', 'source', 'count_subscribers', 'updated_at'
    list_display_links = 'id',
    ordering = '-updated_at',
