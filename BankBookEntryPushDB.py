from aupay import DLfromAuPay
from insertDB import selectDB, importAupayCardCSV, importAupayCSV, insertDB, importMufgCSV
from sendLINE import SendPushDBLINE
import glob, shutil, os, sys

if __name__ == '__main__':
    flag = DLfromAuPay()
    zips = glob.glob("./data/*.zip")
    try:
        shutil.unpack_archive(zips[0], './data/aupay/')
    except IndexError:
        SendPushDBLINE(IndexError, False, 0)
        sys.exit()

    del_files = glob.glob("./data/aupay/auKANTAN*.csv")
    del_files += zips
    for del_file in del_files:
        os.remove(del_file)
    
    aupay_f = glob.glob("./data/aupay/auPAY_20*.csv")
    aupay_f.sort()
    aupaycard_f = glob.glob("./data/aupay/auPAY_Card*.csv")
    aupaycard_f.sort()
    mufg_f = glob.glob("./data/mufg/*.csv")
    mufg_f.sort()

    genre_list = selectDB()
    insert_list = importAupayCSV(aupay_f[-1], genre_list)
    insert_list += importAupayCardCSV(aupaycard_f[-1], genre_list)
    insert_list += importMufgCSV(mufg_f[-1])
    insert_list = sorted(insert_list, key=lambda x:(x[2], x[3]))
    try:
        insertDB(insert_list)
    except TypeError:
        SendPushDBLINE(TypeError, False, 1)
        sys.exit()
    SendPushDBLINE([aupay_f[-1][19:23], aupay_f[-1][23:25], len(insert_list)], True, 0)