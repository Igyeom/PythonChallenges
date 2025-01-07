def readposint():
    s = input()
    try:
        int(s)
    except ValueError:
        return None

    if int(s) > 0:
        return int(s)
    else:
        return None

print(readposint())
