import sqlite3


def savetosql(dictionary: dict, path):
    connect = sqlite3.connect(path)
    sql_str = "INSERT INTO csinf_skininfo(name,steam_price,market_price,market_order,buff_price,buff_order, sb,sm,mb,ms,bm, bs,market_7d,num_sell_buff,num_order_buff, buff_link,market_link,steam_link) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    for skin_num in range(len(dictionary['Name'])):
        info = [
            dictionary['Name'][skin_num],
            dictionary['Steam price'][skin_num],
            dictionary['Market price'][skin_num],
            dictionary['Market order'][skin_num],
            dictionary['Buff price'][skin_num],
            dictionary['Buff order'][skin_num],
            dictionary['S/B'][skin_num],
            dictionary['S/M'][skin_num],
            dictionary['M/B'][skin_num],
            dictionary['M/S'][skin_num],
            dictionary['B/M'][skin_num],
            dictionary['B/S'][skin_num],
            dictionary['Market7D'][skin_num],
            dictionary['NumSellBuff'][skin_num],
            dictionary['NumOrderBuff'][skin_num],
            dictionary['Buff Link'][skin_num],
            dictionary['Market Link'][skin_num],
            dictionary['Steam Link'][skin_num]
        ]
        cur = connect.cursor()
        cur.execute(sql_str, info)
        connect.commit()
    connect.close()
