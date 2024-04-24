import flask
import psycopg2

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:SlateBlue">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>')
def my_sum(num1, num2):
    num1int = int(num1)
    num2int = int(num2)
    sum = num1int + num2int
    return str(sum)

@app.route('/pop/<state>')
def state_population(state):
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

    return str(row_list[1])

if __name__ == '__main__':
    my_port = 5120
    app.run(host='0.0.0.0', port = my_port) 
