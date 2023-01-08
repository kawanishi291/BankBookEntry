from insertDB import connectDB
from sendLINE import SendBackupDBLINE

def selectTable(table):
    conn = connectDB()
    cur = conn.cursor()
    cur.execute('SELECT * from ' + table)
    results = cur.fetchall()

    return results


if __name__ == '__main__':
    f = open('./data/sql/init.sql', 'w')

    genre_list = selectTable("top_genre")
    last = len(genre_list)
    f.write("INSERT INTO top_genre (name, type) VALUES\n")
    for row in genre_list:
        ID, NAME, TYPE = row
        if last == ID:
            f.write("('" + NAME + "','" + TYPE + "')" + ";\n")
        else:
            f.write("('" + NAME + "','" + TYPE + "')" + ",\n")
    f.write("COMMIT;\n\n")

    payment_list = selectTable("top_payment")
    last = len(payment_list)
    f.write("INSERT INTO top_payment (name, date, time, type, price) VALUES\n")
    for row in payment_list:
        ID, NAME, DATE, TIME, TYPE, PRICE = row
        if last == ID:
            f.write("('" + NAME + "','" + str(DATE) + "','" + str(TIME) + "','" + TYPE +  "','" + str(PRICE) + "')" + ";\n")
        else:
            f.write("('" + NAME + "','" + str(DATE) + "','" + str(TIME) + "','" + TYPE +  "','" + str(PRICE) + "')" + ",\n")
    f.write("COMMIT;\n\n")

    color_list = selectTable("top_color")
    last = len(color_list)
    f.write("INSERT INTO top_color (code, type) VALUES\n")
    for row in color_list:
        ID, CODE, TYPE = row
        if last == ID:
            f.write("('" + CODE + "','" + TYPE + "')" + ";\n")
        else:
            f.write("('" + CODE + "','" + TYPE + "')" + ",\n")
    f.write("COMMIT;\n\n")

    # ProcessCheck
    # process_check_list = selectTable("top_processcheck")
    conn = connectDB()
    cur = conn.cursor()
    cur.execute('SELECT top_processcheck.id, top_processcheck.payment_id, top_processcheck.flag, top_processcheck.payer, top_processcheck.charge \
        FROM top_processcheck INNER JOIN top_payment ON top_processcheck.payment_id=top_payment.id')
    process_check_list = cur.fetchall()
    last = len(process_check_list)
    f.write("INSERT INTO top_processcheck (payment, flag, payer, charge) VALUES\n")
    for row in process_check_list:
        ID, PAYMENT, FLAG, PAYER, CHARGE = row
        if FLAG:
            flag = "True"
        else:
            flag = "False"
        if CHARGE:
            charge = "True"
        else:
            charge = "False"
        if last == ID:
            f.write("('" + str(PAYMENT) + "','" + flag + "','" + str(PAYER) + "','" + charge + "')" + ";\n")
        else:
            f.write("('" + str(PAYMENT) + "','" + flag + "','" + str(PAYER) + "','" + charge + "')" + ",\n")
    f.write("COMMIT;\n\n")

    f.close()

    SendBackupDBLINE()