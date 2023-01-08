import datetime
import os
import shutil
import pandas as pd

def CopyCSV(file):
    now = datetime.datetime.now()
    file_name = now.strftime('%Y%m%d')
    if file == "./data/goriyourireki.csv":
        shutil.copy(file, './data/aupaycard/' + file_name + '.csv')
        os.remove(file)

        return './data/aupaycard/' + file_name + '.csv'
    else:
        shutil.copy(file, './data/mufg/' + file_name + '.csv')
        os.remove(file)

        return './data/mufg/' + file_name + '.csv'


def importCSV(file_name):
    df = pd.read_csv(file_name, encoding="Shift-JIS")

    item_list = []
    sumprice = 0
    if file_name.find('aupaycard') == -1:
        for index, data in df.iterrows():
            if str(data['摘要内容']).find('ヤチン') != -1:
                sumprice = int(str(data['支払い金額']).replace(',', ''))
                item_list.append([str(data['日付'])[5:], str(data['摘要内容']), format(sumprice, ',')])
    else:
        for index, data in df.iterrows():
            sumprice += data['利用金額']
            item_list.append([str(data['利用日'])[5:], str(data['利用店名']), format(int(data['利用金額']), ',')])

    return item_list, sumprice