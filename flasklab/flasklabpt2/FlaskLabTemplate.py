from flask import Flask
from flask import render_template
import psycopg2

app = Flask(__name__)

@app.route("/")
def startScreen():
    return render_template("index.html")

@app.route('/rand')
def randomGame():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mosesm2",
        user="mosesm2",
        password="field599farm")
    
    cur = conn.cursor()

    sql = """SELECT * FROM videogames  
            ORDER BY RANDOM()  
            LIMIT 1;"""

    cur.execute(sql)

    row = cur.fetchone()

    return render_template("random.html", randGame = str(row[0]), console = str(row[1]))

if __name__ == '__main__':
    my_port = 5120
    app.run(host='0.0.0.0', port = my_port) 