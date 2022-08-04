from django.contrib import admin

# Register your models here.
from csinf.models import SkinInfo


class SkinInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'steam_price', 'market_price', 'buff_price')





admin.site.register(SkinInfo, SkinInfoAdmin)

