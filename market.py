from flask import Flask

app = Flask(__name__)


@app.route('/')  # root url of website
def hello_world():
    return '<h1>Hello World! Big words</h1>'
