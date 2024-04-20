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

    cityPop = 0

    for row in row_list:
        if (row[1] > cityPop):
            cityPop = row[1]
            largestCityPop = row[0]
        
    print(largestCityPop)
    return None

def test_query_smallest_city_mn():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mosesm2",
        user="mosesm2",
        password="field599farm")
    
    cur = conn.cursor()

    sql1 = """SELECT * FROM cities
            JOIN states;"""
    
    sql2 = """CREATE VIEW cities_states AS SELECT city, city_population, code, state
            WHERE code = 'MN' """

    cur.execute(sql1, sql2)

    row_list = cur.fetchall()

    cityPop = row[1]

    for row in row_list:
        if (cityPop <= row[1]):
            cityPop = row[1]
            smallestCityPop = row[0]

    print(smallestCityPop)
    return None



print( test_query_northfield() )
print( test_query_largest_city() )
print( test_query_smallest_city_mn)
    


    


