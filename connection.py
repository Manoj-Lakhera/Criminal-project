import pymysql

def Connect():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='Apple9876!',
        database='criminalSafety'
    )
    return conn  