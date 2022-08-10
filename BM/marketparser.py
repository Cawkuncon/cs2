import requests


def market_parser(game):
    link_game = ''
    link_req = ''
    if game == 'csgo':
        link_game = 'https://market.csgo.com/item/'
        link_req = 'https://market.csgo.com/api/v2/prices/class_instance/RUB.json'
    elif game == 'dota2':
        link_game = 'https://market.dota2.net/item/'
        link_req = 'https://market.dota2.net/api/v2/prices/class_instance/RUB.json'
    request = requests.get(f'{link_req}').json()
    dict_market = dict()
    for item in request['items']:
        name = request['items'][item]['market_hash_name']
        req = request['items'][item]
        if dict_market.get(name):
            if float(req.get('price')) < float(dict_market[name]['price']):
                if dict_market[name].get('popularity_7d'):
                    popularity = int(dict_market[name]['popularity_7d'])
                else:
                    popularity = 1
                dict_market[name] = dict()
                dict_market[name]['price'] = req.get('price', 1)
                if req.get('buy_order'):
                    dict_market[name]['buy_order'] = req.get('buy_order')
                else:
                    dict_market[name]['buy_order'] = 1
                if req.get('avg_price'):
                    dict_market[name]['avg_price'] = req.get('avg_price')
                else:
                    dict_market[name]['avg_price'] = 1
                if req.get('popularity_7d'):  # !!!!
                    if int(req.get('popularity_7d')) > popularity:
                        dict_market[name]['popularity_7d'] = req.get('popularity_7d')
                    else:
                        dict_market[name]['popularity_7d'] = popularity
                else:
                    dict_market[name]["popularity_7d"] = popularity
                dict_market[name]['link'] = f'{link_game}{item.replace("_", "-")}'
                try:
                    dict_market[name]['ratio_price_order'] = float(req.get('price', 1)) / float(req.get('buy_order', 1))
                except ZeroDivisionError:
                    dict_market[name]['ratio_price_order'] = float(req.get('price', 1)) / (
                            float(req.get('buy_order', 1)) + 1)
        else:
            dict_market[name] = dict()
            dict_market[name]['price'] = req.get('price', 1)
            if req.get('buy_order'):
                dict_market[name]['buy_order'] = req.get('buy_order', 1)
            else:
                dict_market[name]['buy_order'] = 1
            dict_market[name]['avg_price'] = req.get('avg_price', 1)
            if req.get('popularity_7d'):
                dict_market[name]['popularity_7d'] = req.get('popularity_7d', 1)
            else:
                dict_market[name]['popularity_7d'] = 1
            dict_market[name]['link'] = f'{link_game}{item.replace("_", "-")}'
            try:
                dict_market[name]['ratio_price_order'] = float(req.get('price', 1)) / float(req.get('buy_order', 1))
            except ZeroDivisionError:
                dict_market[name]['ratio_price_order'] = float(req.get('price', 1)) / (
                        float(req.get('buy_order', 1)) + 1)
    print('parser market end')
    return dict_market
