def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

array = ["Apples", "Bananas", "Pineapples", "Lettuce", "Spinach"]
print(linear_search(array, "Bananas"))
print(linear_search(array, "Spinach"))
print(linear_search(array, "Lemons"))
