from flask import Flask ,redirect
from flask.globals import request
from flask.templating import render_template
from flask.json import jsonify
from day13.dao_emp import DaoEmp
app = Flask(__name__)
 
@app.route('/')
def main():
    return redirect("/static/emp.html")

@app.route('/fetch' , methods=['POST'])
def fetch():
    menu = request.form['menu']
    print(menu)
    return jsonify(result = "ok")

@app.route('/emp_list' , methods=['POST'])
def emp_list():
    de = DaoEmp()
    list = de.selectList()
    print(list)
    return jsonify(list = list)

if __name__ == '__main__':
    app.run(host="localhost", debug=True)
