import sqlite3

conn = sqlite3.connect('Fastcars.sql')

def print_all_cars():
    with conn:
        cur = conn.execute("SELECT id, Name, TopSpeed from Cars")
    
    for row in cur:
        print("ID ",row[0])
        print("Name: ",row[1])
        print("Top Speed: ",row[2],"mph\n")
    print("The End")

def print_one_row():
    with conn:
        PrintCar = input("Car ID:")
    cur = conn.execute("SELECT id, Name, TopSpeed FROM Cars WHERE id = ?", (PrintCar,))
    row = cur.fetchone()
    if row:
        print("ID:",row[0],"Name:",row[1],"Top Speed:",row[2],"mph")
    else:
        print("Invalid ID (must be an integer between 1 and 50, inclusive).") # how do i claim the bonus 25 points??
        print_one_row()

print_all_cars()
print_one_row()
