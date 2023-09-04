def run():
    numbers = list(map(int, input("List of numbers (space-separated): ").split()))
    
    idx = 1
    ans = -1
    
    for i in numbers:
        try:
            if abs(i-numbers[idx]) < ans or ans == -1:
                ans = abs(i-numbers[idx])
            idx += 1
        except IndexError:
            break
    
    print(ans)