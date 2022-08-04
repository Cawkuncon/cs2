from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.forms import widgets

market_choice = (
    ('S', 'steam'),
    ('M', 'market'),
    ('B', 'buff'),
)


class SkinInfo(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя предмета')
    steam_price = models.FloatField(verbose_name='Цена в стиме')
    market_price = models.FloatField(verbose_name='Цена на маркете')
    market_order = models.FloatField(verbose_name='Ордер на покупку на маркете')
    buff_price = models.FloatField(verbose_name='Цена на баффе')
    buff_order = models.FloatField(verbose_name='Цена ордера на баффе')
    sb = models.FloatField(verbose_name='Отношение цены стима к баффу')
    sm = models.FloatField(verbose_name='Отношение цены стима к маркету')
    mb = models.FloatField(verbose_name='Отношение цены маркета к баффу')
    ms = models.FloatField(verbose_name='Отношение цены маркета к стиму')
    bm = models.FloatField(verbose_name='Отношение цены баффа к маркету')
    bs = models.FloatField(verbose_name='Отношение цены баффа к стиму')
    market_7d = models.IntegerField(blank=True, null=True, verbose_name='Количество покупок 7 дней на маркете')
    num_sell_buff = models.IntegerField(blank=True, null=True, verbose_name='Количество предметов на баффе')
    num_order_buff = models.IntegerField(blank=True, null=True, verbose_name='Количество ордеров на баффе')
    buff_link = models.URLField(blank=True, null=True, verbose_name='Ссылка на бафф')
    market_link = models.URLField(blank=True, null=True, verbose_name='Ссылка на маркет')
    steam_link = models.URLField(blank=True, null=True, verbose_name='Ссылка на стим')

    def get_image_url(self):
        return f'https://cdn.csgo.com//item/{self.name}/300.png'

    class Meta:
        ordering = ['steam_price']

    def __str__(self):
        return self.name

