import os, sys
import django
from pathlib import Path

project = Path(__file__).resolve().parent.parent
sys.path.append(str(project))
os.environ['DJANGO_SETTINGS_MODULE'] = 'cs2.settings'
django.setup()

from csinf.models import SkinInfo

objects_exists = SkinInfo.objects.all()

def djangosavetosql(dictsave: dict):
    for num_skin in range(len(dictsave['Name'])):
        new_skin_dict = {
            'name': dictsave['Name'][num_skin],
            'steam_price': dictsave['Steam price'][num_skin],
            'market_price': dictsave['Market price'][num_skin],
            'market_order': dictsave['Market order'][num_skin],
            'buff_price': dictsave['Buff price'][num_skin],
            'buff_order': dictsave['Buff order'][num_skin],
            'sb': dictsave['S/B'][num_skin],
            'sm': dictsave['S/M'][num_skin],
            'mb': dictsave['M/B'][num_skin],
            'ms': dictsave['M/S'][num_skin],
            'bm': dictsave['B/M'][num_skin],
            'bs': dictsave['B/S'][num_skin],
            'market_7d': dictsave['Market7D'][num_skin],
            'num_sell_buff': dictsave['NumSellBuff'][num_skin],
            'num_order_buff': dictsave['NumOrderBuff'][num_skin],
            'buff_link': dictsave['Buff Link'][num_skin],
            'market_link': dictsave['Market Link'][num_skin],
            'steam_link': dictsave['Steam Link'][num_skin],
        }
        SkinInfo.objects.update_or_create(name=dictsave['Name'][num_skin], defaults=new_skin_dict)
        # try:
        #     SkinInfo.objects.filter(name=dictsave['Name'][num_skin])[0].update(**new_skin_dict)
        # except Exception:
        #     SkinInfo.objects.create(**new_skin_dict)
