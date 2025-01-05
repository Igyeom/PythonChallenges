import sqlite3

conn = sqlite3.connect('Fastcars.sql')

def add_car():
    with conn:
        NewCarName = input("Car Name: ")
        NewCarSpeed = input("Top Speed of car: ")
        conn.execute("INSERT INTO Cars(Name,TopSpeed) VALUES(?,?)", (NewCarName,NewCarSpeed))

def del_car():
    with conn:
        DeleteCar = input("Car ID for deletion:")
        cur = conn.execute("SELECT * FROM Cars WHERE id = ?", (DeleteCar,))
        print(f"Are you sure you'd like to delete the following record?")
        for row in cur:
            print(row, end=' ')
        print()
        confirm = input("(y/n) ") # bonus points where
        if confirm.lower() == "y":
            conn.execute("DELETE FROM Cars WHERE id = ?", (DeleteCar,))
            print("Successfully removed the record.")
        else:
            return

del_car()
