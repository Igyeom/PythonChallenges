with open("counter.txt","r") as existing_file:
    start = int([i for i in existing_file.read().splitlines() if i != ""][-1])+1
with open("counter.txt","a") as existing_file:
    for i in range(start,start+10):
        line_to_write = str(i)+"\n"
        existing_file.write(line_to_write)
