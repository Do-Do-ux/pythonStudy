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
e_id = "4"
e_name = "4"
gen = "4"
addr = "4"



sql = f"""
    INSERT INTO emp
        (e_id,e_name,gen,addr) 
    VALUES
        ('{e_id}','{e_name}','{gen}','{addr}')
"""


cnt = cur.execute(sql)
print(cnt)
print(cur.rowcount)
if cnt > 0:
    con.commit()
    print("완료")
    

con.close()    
