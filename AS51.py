import sqlite3

conn = sqlite3.connect('Fastcars.sql')

def update_a_car():
    with conn:
        update_car = input("Car id to update:")
        cur = conn.execute("SELECT id, Name, TopSpeed FROM Cars WHERE id = ?", (update_car,))
        row = cur.fetchone()
        print("ID:",row[0],"Name:",row[1],"Top Speed:",row[2],"mph")
        car_top_speed = input("The new top speed is:")
        conn.execute("UPDATE Cars SET TopSpeed=? WHERE id=?", (car_top_speed, update_car))
        print(f"New Value: {car_top_speed}") # bonus points where got
