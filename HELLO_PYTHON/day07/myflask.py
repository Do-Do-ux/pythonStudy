from flask import Flask, redirect
from flask.templating import render_template
from flask.globals import request
 
app = Flask(__name__)
 
@app.route('/')
def main():
    return 'hello flask'

@app.route('/param')
def param():
    menu = request.args.get('menu','짬뽕')
    return 'PARAM'+menu

@app.route('/post' ,methods = ['POST','GET'])
def post():
        menu = request.form.get('menu')
        return "POST:" + menu
    
@app.route('/forw')
def forw():
    a = "홍길동"
    b = ["선동렬","장종훈"]
    c = [
        {'e_id':'1','e_name':'1','gen':'1','addr':'1',},
        {'e_id':'2','e_name':'2','gen':'2','addr':'2',},
        {'e_id':'3','e_name':'3','gen':'3','addr':'3',}
        ] 
    
    return render_template("forw.html", a=a,b=b,c=c)

if __name__ == '__main__':
    app.run(host="localhost",debug=True)