from flask import Flask, redirect
from flask.templating import render_template
from flask.globals import request
import pymysql
from day09.dao_emp import DaoEmp
 




app = Flask(__name__)
                                #Dictionary
@app.route('/')
@app.route('/emp_list')

def emp_list():
    de = DaoEmp()
    list = de.selectList()
    
    return render_template("emp_list.html", list=list)

@app.route('/emp_detail')

def emp_detail():
    de = DaoEmp()
    e_id = request.args.get('e_id','1')
    one = de.selectOne(e_id)
    
    return render_template("emp_detail.html", one=one)

@app.route('/emp_mod')

def emp_mod():
    de = DaoEmp()
    e_id = request.args.get('e_id','1')
    one = de.selectOne(e_id)
    
    return render_template("emp_mod.html", one=one)


@app.route('/emp_mod_act' ,methods=['POST'])
def emp_mod_act():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    gen = request.form['gen']
    addr = request.form['addr']
    de = DaoEmp()
    one = de.update(e_id, e_name, gen, addr)
    print(one)
    
    return render_template("emp_mod_act.html", one=one)



    


if __name__ == '__main__':
    app.run(host="localhost",debug=True)