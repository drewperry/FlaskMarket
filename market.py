from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')  # root url of website
def home_page():
    return render_template('home.html')


