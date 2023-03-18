from django.contrib import admin
from django.utils.safestring import mark_safe

from core.models import Chapter, Manga, Page


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "popularity_index", "rating")


class PageInline(admin.StackedInline):
    model = Page
    extra = 0
    readonly_fields = ("image_presentation", "image_colored_presentation")
    exclude = ("colored_file",)

    def image_presentation(self, obj):
        result = f'<a href="{obj.file.url}" target="_blank"><img src="{obj.file.url}" width="500px"/></a>'
        return mark_safe(result)

    def image_colored_presentation(self, obj):
        if obj.colored_file:
            result = (
                f'<a href="{obj.colored_file.url}" target="_blank">'
                f'<img src="{obj.colored_file.url}" width="500px"/></a>'
            )
            return mark_safe(result)
        return None


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ("id", "manga", "number")

    inlines = (PageInline,)
