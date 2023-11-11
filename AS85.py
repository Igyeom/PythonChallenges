with open("if.txt", "r+") as f:
    content_1 = f.read().lower().splitlines()
    count_1 = 0

    for line in content_1:
        count_1 += line.split().count("if")
    

    with open("mam.txt", "r+") as g:
        content_2 = g.read().lower().splitlines()
        count_2 = 0

        for line in content_2:
            count_2 += line.split().count("if")
        
        f.write("\n\n\n\nIf Count: " + str(count_1))
        f.write("\nMore If occurrences?: " + str(count_1 > count_2))
        g.write("\n\n\n\nIf Count: " + str(count_2))
        g.write("\nMore If occurrences?: " + str(count_2 > count_1))

print("If Count complete. Wrote results to the files.")

# this program may require these text files: https://drive.google.com/drive/u/0/folders/1m07L76tn0oKGn5eLLs3d81t1YnGcFoBo
