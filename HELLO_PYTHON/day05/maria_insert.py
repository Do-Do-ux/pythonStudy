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
e_name = "6"
gen = "6"
addr = "7"



sql = f"""
    update emp
    
    set 
        e_id = {e_id},
        e_name = {e_name},
        gen = {gen},
        addr = {addr}
    
    where
        e_id = {e_id}
"""


cnt = cur.execute(sql)
print(cnt)
print(cur.rowcount)
if cnt > 0:
    con.commit()
    print("완료")
    

con.close()    
