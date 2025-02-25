def gray(n: int):
    if n == 1:
        return ["0", "1"]
    return ["0"+i for i in gray(n-1)]+["1"+i for i in gray(n-1)[::-1]]
    

print(gray(int(input())))
