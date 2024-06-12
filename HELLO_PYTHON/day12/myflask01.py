from flask import Flask
from flask.globals import request
from flask.templating import render_template
from flask.json import jsonify
app = Flask(__name__)
 
@app.route('/')
def main():
    return 'Hello'

@app.route('/ajax1' , methods=['POST'])
def ajax1():
    return jsonify(result = 1)
@app.route('/ajax2' , methods=['POST'])
def ajax2():
    return jsonify(result = 2)

if __name__ == '__main__':
    app.run(host="localhost", debug=True)
