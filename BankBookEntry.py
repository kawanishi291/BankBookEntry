from aupaycard import DLfromAuPayCard
from mufg import DLfromMUFG
from importCSV import importCSV, CopyCSV
from insertDB import importDB, updateDB
from sendLINE import SendLINE
import glob


if __name__ == '__main__':
    flag = DLfromAuPayCard()
    DLfromMUFG()
    payment = 0
    msg_list = []
    message = ""
    files = glob.glob("./data/*.csv")
    for file in files:
        file_name = CopyCSV(file)
        item_list, sumprice = importCSV(file_name)
        payment += sumprice
        msg_list += item_list
    item_list, sumprice, update_list = importDB()
    msg_list += item_list
    for i in msg_list:
        message += str(i[0]) + " : ¥" + str(i[2]) + "\n" + str(i[1]) + "\n"

    SendLINE(flag, format((payment // 2) + sumprice, ','), message)
    if flag:
        updateDB(update_list)
    