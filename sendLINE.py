import requests
from Info import Info


def SendLINE(flag, payment, send_contents):
    info = Info()
    URL = info.get('LINE', 'URL')
    TOKEN = info.get('LINE', 'TOKEN')

    #情報を辞書型にする
    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN} 
    if flag:
        send_dic = {'message': "\n【今月分の振り込み金額】\n¥" + payment + "\n\n【詳細】\n" + send_contents}
    else:
        send_dic = {'message': "\nDownload Error\n明細が正常にダウンロード出来ませんでした" }
    #LINE通知を送る（200: 成功時、400: リクエストが不正、401: アクセストークンが無効：公式より）
    requests.post(URL, headers=TOKEN_dic, data=send_dic)


def SendPushDBLINE(send_contents_list, flag, status):
    info = Info()
    URL = info.get('LINE', 'URL')
    TOKEN = info.get('LINE', 'TOKEN')

    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
    if flag == True:
        send_dic = {'message': "\n" + str(send_contents_list[0]) + "年" + str(send_contents_list[1]) + \
             "月分のデータ" + str(send_contents_list[2]) + "件をDBに格納致しました"}
    elif status == 0:
        send_dic = {'message': "\nDownload Error\n明細が正常にダウンロード出来ませんでした" }
    elif status == 1:
        send_dic = {'message': "\nINSERT DB Error\n正常にデータベースに登録できませんでした" }

    requests.post(URL, headers=TOKEN_dic, data=send_dic)


def SendBackupDBLINE():
    info = Info()
    URL = info.get('LINE', 'URL')
    TOKEN = info.get('LINE', 'TOKEN')

    #情報を辞書型にする
    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN} 
    send_dic = {'message': "\nDBのバックアップ処理完了致しました" }

    #LINE通知を送る（200: 成功時、400: リクエストが不正、401: アクセストークンが無効：公式より）
    requests.post(URL, headers=TOKEN_dic, data=send_dic)