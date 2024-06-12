from flask import Flask
from flask.globals import request
from flask.templating import render_template
app = Flask(__name__)
 
@app.route('/')
def main():
    return 'Hello, flask!'

if __name__ == '__main__':
    app.run(host="localhost", debug=True)
