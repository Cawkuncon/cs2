from django import forms
from django.forms import ModelForm, HiddenInput

from csinf.models import Notice

variable = [
    (None, 'Выберите параметры сортировки'),
    ('name', 'Имя'),
    ('steam_price', 'Цена стима'),
    ('market_price', 'Цена на маркете'),
    ('market_order', 'Ордер на покупку на маркете'),
    ('buff_price', 'Цена на баффе'),
    ('buff_order', 'Цена ордера на баффе'),
    ('sb', 'Отношение цены стима к баффу'),
    ('sm', 'Отношение цены стима к маркету'),
    ('mb', 'Отношение цены маркета к баффу'),
    ('ms', 'Отношение цены маркета к стиму'),
    ('bm', 'Отношение цены баффа к маркету'),
    ('bs', 'Отношение цены баффа к стиму'),
    ('market_7d', 'Количество покупок за 7 дней на маркете'),
    ('num_sell_buff', 'Количество предметов на баффе'),
    ('num_order_buff', 'Количество ордеров на баффе'),
]

variable2 = [
    (None, 'Выберите параметры указания границ'),
    ('steam_price', 'Цена стима'),
    ('market_price', 'Цена на маркете'),
    ('market_order', 'Ордер на покупку на маркете'),
    ('buff_price', 'Цена на баффе'),
    ('buff_order', 'Цена ордера на баффе'),
    ('sb', 'Отношение цены стима к баффу'),
    ('sm', 'Отношение цены стима к маркету'),
    ('mb', 'Отношение цены маркета к баффу'),
    ('ms', 'Отношение цены маркета к стиму'),
    ('bm', 'Отношение цены баффа к маркету'),
    ('bs', 'Отношение цены баффа к стиму'),
    ('market_7d', 'Количество покупок за 7 дней на маркете'),
    ('num_sell_buff', 'Количество предметов на баффе'),
    ('num_order_buff', 'Количество ордеров на баффе'),
]

min_max = [
    # (None, 'Выберите тип сортировки'),
    ('+', 'По возрастанию'),
    ('-', 'По убыванию'),
]


class FormOrderBy(forms.Form):
    order_by = forms.BooleanField(widget=forms.Select(choices=variable), label='Сортировка', required=False)
    min_max = forms.BooleanField(widget=forms.Select(choices=min_max), label='Опции', required=False)
    filter_num = forms.BooleanField(widget=forms.Select(choices=variable2), label='Выбор значения',
                                    required=False)
    min_value = forms.FloatField(min_value=0, max_value=100000, label='Минимальное значение', required=False)
    max_value = forms.FloatField(min_value=0, max_value=100000, label='Максимальное значение', required=False)


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'
        widgets = {
            'skin_name': HiddenInput(),
        }
        # exclude = ['skin_name', ]
