from Info import Info
import pandas as pd
import pg8000


def importAupayCSV(file_name, genre_list):
    col_names = ['c{0:02d}'.format(i) for i in range(10)]
    df = pd.read_csv(file_name, encoding="Shift-JIS", names = col_names)
    item_list = []
    for index, data in df.iterrows():
        if str(data['c03']).find('nan') == -1:
            if str(data['c03']).find('支払い') != -1:
                i = data['c01'].find(" ")
                date = data['c01'][:i]
                time = data['c01'][i+1:]
                type = next((value for key, value in genre_list.items() if key in data['c02']), '')
                t = (data['c02'], date.replace('/', '-'), time, type, int(data['c04'].replace(',', '')))
                item_list.insert(0,t)

    return item_list

def importAupayCardCSV(file_name, genre_list):
    col_names = ['c{0:02d}'.format(i) for i in range(10)]
    df = pd.read_csv(file_name, encoding="Shift-JIS", names = col_names)
    item_list = []
    for index, data in df.iterrows():
        if str(data['c03']).find('nan') == -1:
            if str(data['c02']).find('ａｕ　ＰＡＹ　残高') == -1:
                if str(data['c02']) != '利用店舗':
                    date = data['c01']
                    time = "0:00"
                    type = next((value for key, value in genre_list.items() if key in data['c02']), '')
                    t = (data['c02'], date.replace('/', '-'), time, type, int(data['c03'].replace(',', '')))
                    item_list.insert(0,t)

    return item_list

def importMufgCSV(file_name):
    df = pd.read_csv(file_name, encoding="Shift-JIS")
    for index, data in df.iterrows():
        name = str(data['摘要内容'])
        if name.find('ニホンセ−フテイ−（カ') != -1:
            price = int(str(data['支払い金額']).replace(',', ''))
            date = str(data['日付']).replace('/', '-')
            type = "家賃"
            return [(name, date, '0:00', type, price)]
        if name.find('ヤチン') != -1:
            price = int(str(data['支払い金額']).replace(',', ''))
            date = str(data['日付']).replace('/', '-')
            type = "家賃"
            return [(name, date, '0:00', type, price)]


def connectDB():
    info = Info()
    USER = info.get('DB', 'USER')
    HOST = info.get('DB', 'HOST')
    DATABASE = info.get('DB', 'DATABASE')
    PASSWORD = info.get('DB', 'PASSWORD')
    conn = pg8000.connect(
        user=USER,
        host=HOST,
        database=DATABASE,
        password=PASSWORD
    )

    return conn


def selectDB():
    genre_list = {}
    conn = connectDB()
    cur = conn.cursor()
    cur.execute('SELECT * FROM top_genre')
    results = cur.fetchall()

    for row in results:
        ID, NAME, TYPE = row
        genre_list[NAME] = TYPE
    
    return genre_list


def insertDB(insert_list):
    conn = connectDB()
    cur = conn.cursor()
    sql = '''
        INSERT INTO top_payment(
        name, date, time, type, price)
        VALUES (%s, %s, %s, %s, %s);
    '''
    for item in insert_list:
        cur.execute(sql, item)
    conn.commit()


def importDB():
    conn = connectDB()
    cur = conn.cursor()
    cur.execute('SELECT top_processcheck.id, top_processcheck.payer, top_processcheck.charge, top_payment.name, top_payment.date, top_payment.price \
        FROM top_processcheck INNER JOIN top_payment ON top_processcheck.payment_id=top_payment.id \
        WHERE top_processcheck.flag=False')
    results = cur.fetchall()
    data_list = []
    update_list = []
    sumprice = 0
    for row in results:
        ID, PAYER, CHARGE, NAME, DATE, PRICE = row
        data_list.append([str(DATE)[5:].replace('-', '/'), NAME, format(PRICE, ',')])
        update_list.append(str(ID))
        price = PRICE
        if CHARGE:
            # 二人負担
            price //= 2
        if PAYER == 1:
            # 妻
            price *= -1
        sumprice += price


    return data_list, sumprice, update_list


def updateDB(update_list):
    update_list.sort()
    conn = connectDB()
    cur = conn.cursor()
    sql = '''
        UPDATE top_processcheck 
        SET flag = True
        WHERE id = %s;
    '''
    for item in update_list:
        cur.execute(sql, item)
    conn.commit()