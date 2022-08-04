import requests


def buff_parser(session, min_price, max_price, game, message_initialization):
    print(message_initialization)
    cookies = {'session': session, }
    total_page = requests.get(
        f'https://buff.163.com/api/market/goods?game={game}&page_num=100000&min_price={min_price}&max_price={max_price}&page_size=80',
        cookies=cookies).json()['data']['total_page']
    page = 1
    dict_items = {}
    print(f'total page {total_page}')
    while page <= total_page: #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print(page)
        page_json = requests.get(
            f'https://buff.163.com/api/market/goods?game={game}&page_num={page}&min_price={min_price}&max_price={max_price}&page_size=80',
            cookies=cookies).json()
        if page_json['code'] == 'OK':
            page_dict = page_json['data']['items']
            for item in page_dict:
                name_item = item['market_hash_name']
                dict_items[name_item] = dict()
                dict_items[name_item]['buy_order'] = item.get('buy_max_price', 1)
                dict_items[name_item]['count_buy'] = item.get('buy_num', 1)
                dict_items[name_item]['steam_price'] = item['goods_info'].get('steam_price', 1)
                dict_items[name_item]['steam_price_cny'] = item['goods_info'].get('steam_price_cny', 1)
                dict_items[name_item]['buff_link'] = f'https://buff.163.com/goods/{item.get("id")}'
                dict_items[name_item]['price'] = item.get('sell_min_price', 1)
                dict_items[name_item]['count_sell'] = item.get('sell_num', 1)
                dict_items[name_item]['steam_link'] = item.get('steam_market_url')
        page += 1
    print('parser buff end')
    return dict_items
