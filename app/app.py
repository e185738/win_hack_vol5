from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/send', methods=["post", "get"])
def post():

    dns = mysql.connector.connect(
        user='root',
        host='localhost',
        password='root',
        database='vol5_db'
    )  # dbの接続情報

    cur = dns.cursor()  # db操作用のカーソル

    if request.method == 'POST':
        ms = request.form["message"]
        print(ms)

        stmt = 'INSERT INTO message(ms) VALUES("{0}")'.format(ms)

        cur.execute(stmt)

        dns.commit()
        dns.close()

        return render_template('send.html', ms=ms)
    if request.method == 'GET':
        stmt = 'SELECT * FROM message ORDER BY RAND()'

        cur.execute(stmt)
        ms = cur.fetchone()[0]

        dns.close()
        return render_template('send.html', ms=ms)
    else:
        return 'error'
