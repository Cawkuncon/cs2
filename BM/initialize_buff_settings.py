import os

import requests
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

min_price = int(os.environ.get('MIN_PRICE_CNY'))
max_price = int(os.environ.get('MAX_PRICE_CNY'))
if min_price > max_price:
    raise ValueError('Максимальная цена ниже минимальной')
session = os.environ.get('SESSION')
game = os.environ.get('GAME')
code = requests.get(
    f'https://buff.163.com/api/market/goods?game={game}&page_num=100000&min_price={min_price}&max_price={max_price}',
    cookies={'session': session, }).json()['code']
if code != 'OK':
    raise ValueError('Ошибка запроса к серверу, проверьте куки и параметры в запросе')
message_initialization = 'success'
