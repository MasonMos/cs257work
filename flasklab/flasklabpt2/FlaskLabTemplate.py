from flask import Flask
from flask import render_template
import psycopg2

app = Flask(__name__)

@app.route("/")
def startScreen():
    return render_template("index.html")

@app.route('/rand')
def state_population():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mosesm2",
        user="mosesm2",
        password="field599farm")
    
    cur = conn.cursor()

    sql = "SELECT * FROM states WHERE code = %s;"

    cur.execute(sql, [state])

    row = cur.fetchone()

    return str(row[2])

if __name__ == '__main__':
    my_port = 5120
    app.run(host='0.0.0.0', port = my_port) 