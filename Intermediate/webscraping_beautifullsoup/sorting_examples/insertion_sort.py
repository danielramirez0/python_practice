test_array = [102, 12, 193, 1932, 192, 11, 293, 39, 239]

def insertion_sort(arr, length):
    i = 1
    while i<length:
        insertion_ith(arr, i)
        i +=1

def insertion_ith(arr, i):
    key = arr[i]
    j = i -1 
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1] = key

print(test_array)
insertion_sort(test_array, len(test_array))
print(test_array)