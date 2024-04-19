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

def test_query_largest_city():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mosesm2",
        user="mosesm2",
        password="field599farm")
    
    cur = conn.cursor()

    sql = "SELECT city, city_population FROM cities"

    cur.execute(sql)

    row_list = cur.fetchall()

    for row in row_list:
        print(row)

    return None




print( test_query_northfield() )
print( test_query_largest_city() )
    


    


