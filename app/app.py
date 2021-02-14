from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect("host=127.0.0.1 port=5432 dbname=vol5_db user=flask_user")
cur = conn.cursor()

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/send', methods=["post", "get"])
def post():
    if request.method == 'POST' and len(request.form["message"]) != 0:
        ms = request.form["message"]
        stmt = 'INSERT INTO message(ms) VALUES(\'{0}\')'.format(ms)
        cur.execute(stmt)

        return render_template('send.html', ms=ms)
    if request.method == 'GET':
        stmt = 'SELECT * FROM message ORDER BY random() LIMIT 1'
        cur.execute(stmt)
        ms = cur.fetchone()[0]

        return render_template('send.html', ms=ms)
    else:
        return render_template('home.html')
