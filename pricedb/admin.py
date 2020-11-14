from django.contrib import admin
from .models import SearchHistory, RealEstateProperty
from django.utils.html import format_html

class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')

class RealEstatePropertyAdmin(admin.ModelAdmin):
    ordering = ('price',)
    list_display = ('name', 'page_url', 'price', 'image_img')

    def page_url(self, obj):
        if obj.link:
            return format_html(f'<a href="{obj.link}">{obj.link}</a>')
        else:
            return ''

    def image_img(self, obj):
        if obj.image:
            return format_html('<img src="%s" width="100px"/>' % obj.image)
        else:
            return ''

    image_img.short_description = 'Image'
    image_img.allow_tags = True
    page_url.short_description = 'Link'

admin.site.register(SearchHistory, SearchHistoryAdmin)
admin.site.register(RealEstateProperty, RealEstatePropertyAdmin)
