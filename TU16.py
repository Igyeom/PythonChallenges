# Exercise 1
ringgit = 129.00
print(f"RM{ringgit:.0f}")

# Exercise 2
numcol1 = [1,1003442,5.32222342]
numcol2 = [5.62233,7.364363,9.32747474342]
numcol3 = [9.2634526,7.866832817,10.781237892798]

heading1 = "Outlier Effect"
heading2 = "Normal Data 1"
heading3 = "Normal Data 2"
print(f"{heading1:^15} {heading2:^15} {heading3:^15}")
for i in range(3):
    print(f"{numcol1[i]:^15.2f} {numcol2[i]:^15.2f} {numcol3[i]:^15.2f}")

# Exercise 3
number = int(input("Denary: "))
print(f"Binary: {number:b}")
