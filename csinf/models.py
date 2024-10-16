# from django.contrib.auth.models import AbstractUser
import datetime

from django.core.validators import MinValueValidator
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


class Notice(models.Model):
    """добавить юзера через foreignkey"""
    username_notice = models.ForeignKey('accounts.MyUser', on_delete=models.CASCADE, null=True, blank=True)
    skin_name = models.ForeignKey(SkinInfo, on_delete=models.CASCADE, null=True, blank=True)
    buy_from = models.CharField(choices=market_choice, default='S', max_length=1)
    sell_to = models.CharField(choices=market_choice, default='B', max_length=1)
    buy_price = models.FloatField()
    sell_price = models.FloatField()
    count_skins = models.IntegerField(validators=[MinValueValidator(1), ], blank=True, null=True)
    text_notice = models.TextField(blank=True)
    date_notice = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_notice']

    def get_date(self):
        return datetime.datetime.strftime(self.date_notice, '%d.%m.%Y %H:%M:%S')

    def get_buy_from(self):
        return dict(market_choice).get(self.buy_from)

    def get_sell_to(self):
        return dict(market_choice).get(self.sell_to)

    def __str__(self):
        return f'{self.username_notice} {self.skin_name}'
