import mariadb
import sys

try:
    conn = mariadb.connect(
        user="root",
        password="python",
        host="localhost",
        port=3305,
        database="python"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


cur = conn.cursor()
    

select_all_query = "SELECT e_id, e_name, gen, addr from emp" 
cur.execute( select_all_query )

resultset = cur.fetchall()

for e_id, e_name,gen,addr in resultset: 
    print(f"e_id: {e_id}, e_name: {e_name},gen: {gen},addr:{addr}")