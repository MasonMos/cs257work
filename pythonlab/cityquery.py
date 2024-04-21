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
        
    
    return largestCityPop

def test_query_smallest_city_mn():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mosesm2",
        user="mosesm2",
        password="field599farm")
    
    cur = conn.cursor()

    sql = "SELECT * FROM cities WHERE state = 'Minnesota' ;"

    cur.execute(sql)

    row_list = cur.fetchall()

    smallest_row = row_list[0][2]
    smallest_row_name = row_list[0][0]

    for row in row_list:
        if (smallest_row >= row[2]):
            smallest_row = row[2]
            smallest_row_name = row[0]

    return smallest_row_name

def test_query_extereme_points():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mosesm2",
        user="mosesm2",
        password="field599farm")
    
    cur = conn.cursor()

    sql = "SELECT * FROM cities;"

    cur.execute(sql)

    row_list = cur.fetchall()

    northernPoint = row_list[0][3]
    northernPointName = ""
    easternPoint = row_list[0][4]
    easternPointName = ""
    westernPoint = row_list[0][4]
    westernPointName = ""
    southernPoint = row_list[0][3]
    southernPointName = ""

    for row in row_list:
        if(row[3] > northernPoint):
            northernPoint = row[3]
            northernPointName = row[0]
    
    for row in row_list:
        if(row[4] > easternPoint):
            easternPoint = row[4]
            easternPointName = row[0]

    for row in row_list:
        if (westernPoint >= row[4]):
            westernPoint = row[4]
            westernPointName = row[0]
    
    for row in row_list:
        if (southernPoint >= row[3]):
            southernPoint = row[3]
            southernPointName = row[0]
    
    print("This is the most eastern city: " + easternPointName)
    print("This is the most western city: " + westernPointName)
    print("This is the most northern city: " + northernPointName)
    print("This is the most southern city: " + southernPointName)

    return None

def test_query_search():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mosesm2",
        user="mosesm2",
        password="field599farm")
    
    cur = conn.cursor()

    sql = """SELECT city, cities.state, city_population, code 
    from cities join states 
    on states.state = cities.state WHERE code = %s OR cities.state = %s;"""

    stateInput = input("Pick a state or state abbreviation:")

    cur.execute(sql, [stateInput])

    row_list = cur.fetchall()

    totalCityPop = 0

    for row in row_list:
        print(row_list)
    
    return totalCityPop






print( test_query_northfield() )
print( "The largest city in the US is " + test_query_largest_city() )
print( "The smallest city in Minnesota is " + test_query_smallest_city_mn() )
test_query_extereme_points()
test_query_search()
    


    


