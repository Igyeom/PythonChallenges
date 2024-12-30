with open("counter.txt","w") as new_file:
    for i in range(10,0,-1):
        new_file.write(str(i)+"\n")
