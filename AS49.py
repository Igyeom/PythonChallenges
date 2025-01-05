import sqlite3

conn = sqlite3.connect('Fastcars.sql')

def search_by_speed():
    MinSpeed = input("I want a car faster than: ") 
    with conn:
        cur = conn.execute("SELECT TopSpeed, Name FROM Cars WHERE TopSpeed>? ORDER BY TopSpeed", (MinSpeed,))
        for row in cur:
            print(row[0],"mph ",row[1])

search_by_speed()
