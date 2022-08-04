from django.contrib import admin

# Register your models here.
from csinf.models import SkinInfo, Notice


class SkinInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'steam_price', 'market_price', 'buff_price')


class NoticeAdmin(admin.ModelAdmin):
    pass


admin.site.register(SkinInfo, SkinInfoAdmin)
admin.site.register(Notice, NoticeAdmin)
