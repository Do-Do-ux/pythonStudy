import pymysql

con = pymysql.connect(
        user="root",
        password="python",
        host="localhost",
        port=3305,
        database="python"
)

cur = con.cursor(pymysql.cursors.DictCursor) #statement와 똑같다.
                                #Dictionary
sql = "select * from emp"
cur.execute(sql)

    
rows = cur.fetchall()
print(rows[0]['addr']) #튜플의 형태로 가져오게 된다.

for addr in rows:
    print(f"addr:{addr}")

cur.close()
con.close()