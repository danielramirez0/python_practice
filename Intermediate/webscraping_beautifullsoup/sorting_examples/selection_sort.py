
def selection_sort(array, length):
    i = 0
    while i < length:
        j = find_smallest_number(array, i, length - 1)
        swap(array, i, j)
        i += 1

def find_smallest_number(array, start, end):
    i = start
    j = i
    while i <= end:
        if array[i] < array[j]:
            j = i
        i += 1
    return j

def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def display(array):
    i = 0
    while i < len(array):
        print(array[i])
        i += 1

test_array = [102, 12, 193, 1932, 192, 11, 293, 39, 239]

print(test_array)
selection_sort(test_array, len(test_array))
print(test_array)