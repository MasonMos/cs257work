import psycopg2

# Connect to database
conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mosesm2",
        user="mosesm2",
        password="field599farm"
        )

# Open cursor to perform database operations
cur = conn.cursor()

# Create new tables

cityTable = """DROP TABLE IF EXISTS cities;
            CREATE TABLE cities (
            City text,
            state text,
            city_population int,
            Latitude real,
            Longitude real
            );"""
stateTable = """DROP TABLE IF EXISTS states;
            CREATE TABLE states (
            Code text,
            state text
            );"""
cur.execute(cityTable)
cur.execute(stateTable)

conn.commit()