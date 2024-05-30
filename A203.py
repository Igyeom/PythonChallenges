def insertion_sort(arr):
    for i in range(1, len(arr)):
        k = arr[i]

        j = i-1
        while j >= 0 and k < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k
    return arr

print(insertion_sort([12, 11, 13, 5, 6, 58, 67, -62, 0]))
