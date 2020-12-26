from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/send', methods=["post"])
def post():
    ms = request.form["message"]
    print(ms)
    return render_template('send.html', ms=ms)
