print("s=vt (assuming all units are coherent)")
s = input("Displacement (leave blank to leave as unknown): ")
v = input("Velocity (leave blank to leave as unknown): ")
t = input("Time (leave blank to leave as unknown): ")

if s == "":
    print(int(v)*int(t))
elif v == "":
    print(int(s)/int(t))
elif t == "":
    print(int(s)/int(v))
