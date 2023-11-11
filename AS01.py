def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(i,len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

print(bubble_sort([7657, 234, 546, 78, 879, 984375, 3]))
