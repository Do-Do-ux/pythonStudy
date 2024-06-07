from flask import Flask, redirect
from flask.templating import render_template
from flask.globals import request
import pymysql
 




app = Flask(__name__)
                                #Dictionary
@app.route('/')
@app.route('/emp_list')

def forw():
    con = pymysql.connect(
            user="root",
            password="python",
            host="localhost",
            port=3305,
            database="python"
    )
     
    cur = con.cursor(pymysql.cursors.DictCursor) #statement와 똑같다.
    sql = "select * from emp"
    cur.execute(sql)
    
        
    rows = cur.fetchall()
    #print(rows[0]['addr']) #튜플의 형태로 가져오게 된다.
    
    emp_list = [];
    for addr in rows:
        emp_list.append(addr)
    
    cur.close()
    con.close()
    c = emp_list
    
    return render_template("emp_list.html", c=c)

if __name__ == '__main__':
    app.run(host="localhost",debug=True)