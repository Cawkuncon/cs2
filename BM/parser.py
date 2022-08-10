from initialize_buff_settings import session, min_price, max_price, game, message_initialization
from course_dol_rub_cny import CourseCnyRub
from buffparser import buff_parser
from marketparser import market_parser
from djangosavetosql import djangosavetosql

dict_to_save = {
    'Name': [],
    'Steam price': [],
    'Market price': [],
    'Market order': [],
    'Buff price': [],
    'Buff order': [],
    'S/B': [],
    'S/M': [],
    'M/B': [],
    'M/S': [],
    'B/M': [],
    'B/S': [],
    'Market7D': [],
    'NumSellBuff': [],
    'NumOrderBuff': [],
    'Buff Link': [],
    'Market Link': [],
    'Steam Link': [],
}

YR = float(CourseCnyRub().get_course())

buff_dict = buff_parser(session, min_price, max_price, game, message_initialization)
market_dict = market_parser(game)

def r(x):
    return round(x, 2)


if __name__ == '__main__':
    print(f'parser {game}')
    for item in buff_dict:
        market_item = market_dict.get(item)
        if market_item:
            dict_to_save['Name'].append(item)
            dict_to_save['Steam price'].append(buff_dict[item]['steam_price_cny'])
            dict_to_save['Market price'].append(r(float(market_item['price']) / YR))
            dict_to_save['Market order'].append(r(float(market_item['buy_order']) / YR))
            dict_to_save['Buff price'].append(buff_dict[item]['price'])
            dict_to_save['Buff order'].append(buff_dict[item]['buy_order'])
            dict_to_save['S/B'].append(
                r(float(buff_dict[item]['steam_price_cny']) * 0.87 / float(buff_dict[item]['price'])))
            dict_to_save['S/M'].append(
                r(float(buff_dict[item]['steam_price_cny']) * 0.87 / (float(market_item['price']) / YR)))
            dict_to_save['M/B'].append(r(float(market_item['price']) / YR * 0.95 / float(buff_dict[item]['price'])))
            try:
                dict_to_save['M/S'].append(
                    r(float(market_item['price']) / YR * 0.95 / float(buff_dict[item]['steam_price_cny'])))
            except ZeroDivisionError:
                dict_to_save['M/S'].append(r(float(market_item['price']) / YR * 0.95 / 1))
            dict_to_save['B/M'].append(r(float(buff_dict[item]['price']) * 0.975 / (float(market_item['price']) / YR)))
            try:
                dict_to_save['B/S'].append(
                    r(float(buff_dict[item]['price']) * 0.975 / float(buff_dict[item]['steam_price_cny'])))
            except ZeroDivisionError:
                dict_to_save['B/S'].append(r(float(buff_dict[item]['price']) * 0.975 / 1))
            dict_to_save['Market7D'].append(market_item['popularity_7d'])
            dict_to_save['NumSellBuff'].append(buff_dict[item]['count_sell'])
            dict_to_save['NumOrderBuff'].append(buff_dict[item]['count_buy'])
            dict_to_save['Buff Link'].append(buff_dict[item]['buff_link'])
            dict_to_save['Market Link'].append(market_item['link'])
            dict_to_save['Steam Link'].append(buff_dict[item]['steam_link'])
        djangosavetosql(dict_to_save)
