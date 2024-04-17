import psycopg2

# This function checks for northfield data.
def test_query_northfield():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mosesm2",
        user="mosesm2",
        password="field599farm")

    cur = conn.cursor()

    sql = "SELECT city, latitude, longitude FROM cities WHERE city = 'Northfield' "

    cur.execute(sql)

    row = cur.fetchone()

    if row is None:
        print("Northfield is not present in this data.")

    conn.commit()

    return row

print( test_query_northfield() )
    


    


