import psycopg2

# This function checks for northfield data.
def testQueryNorthfield():

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

def testQueryLargestCity():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mosesm2",
        user="mosesm2",
        password="field599farm")
    
    cur = conn.cursor()

    sql = "SELECT city, city_population FROM cities"

    cur.execute(sql)

    rowList = cur.fetchall()

    cityPop = 0

    for row in rowList:
        if (row[1] > cityPop):
            cityPop = row[1]
            largestCityPop = row[0]
        
    
    return largestCityPop

def testQuerySmallestCityMn():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mosesm2",
        user="mosesm2",
        password="field599farm")
    
    cur = conn.cursor()

    sql = "SELECT * FROM cities WHERE state = 'Minnesota' ;"

    cur.execute(sql)

    rowList = cur.fetchall()

    smallestRow = rowList[0][2]
    smallestRowName = rowList[0][0]

    for row in rowList:
        if (smallestRow >= row[2]):
            smallestRow = row[2]
            smallestRowName = row[0]

    return smallestRowName

def testQueryExteremePoints():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mosesm2",
        user="mosesm2",
        password="field599farm")
    
    cur = conn.cursor()

    sql = "SELECT * FROM cities;"

    cur.execute(sql)

    rowList = cur.fetchall()

    northernPoint = rowList[0][3]
    northernPointName = ""
    easternPoint = rowList[0][4]
    easternPointName = ""
    westernPoint = rowList[0][4]
    westernPointName = ""
    southernPoint = rowList[0][3]
    southernPointName = ""

    for row in rowList:
        if(row[3] > northernPoint):
            northernPoint = row[3]
            northernPointName = row[0]
    
    for row in rowList:
        if(row[4] > easternPoint):
            easternPoint = row[4]
            easternPointName = row[0]

    for row in rowList:
        if (westernPoint >= row[4]):
            westernPoint = row[4]
            westernPointName = row[0]
    
    for row in rowList:
        if (southernPoint >= row[3]):
            southernPoint = row[3]
            southernPointName = row[0]
    
    print("This is the most eastern city: " + easternPointName)
    print("This is the most western city: " + westernPointName)
    print("This is the most northern city: " + northernPointName)
    print("This is the most southern city: " + southernPointName)

    return None

def testQuerySearch():

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

    cur.execute(sql, (stateInput, stateInput))

    row_list = cur.fetchall()

    totalCityPop = 0
    stateName = ""

    for row in row_list:
        totalCityPop += row[2]
        stateName = row[1]
        
    print("Here is the total population of all cities in " + stateName + ": " + str(totalCityPop))
    return None






testQueryNorthfield()
print( "The largest city in the US is " + testQueryLargestCity() )
print( "The smallest city in Minnesota is " + testQuerySmallestCityMn() )
testQueryExteremePoints()
testQuerySearch()
    


    


