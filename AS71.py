def run():
    p = list(input("The passcode: "))
    c = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()?<>,.[]{}\:;")
    for i in p:
        for j in c:
            if i == j:
                print(j, end='')