from flask import Flask
from flask.globals import request
from flask.templating import render_template
from flask.json import jsonify
app = Flask(__name__)
 
@app.route('/')
def main():
    return 'Hello'

@app.route('/ajax' , methods=['POST'])
def ajax():
    data = request.get_json()
    print(data['menu'])
    return jsonify(result = "ok")

@app.route('/fetch' , methods=['POST'])
def fetch():
    menu = request.form['menu']
    print(menu)
    return jsonify(result = "ok")


@app.route('/fetch' , methods=['POST'])
def axios():
    menu = request.form['menu']
    print(menu)
    return jsonify(result = "ok")



if __name__ == '__main__':
    app.run(host="localhost", debug=True)
