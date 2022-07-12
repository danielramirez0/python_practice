# slow, grows with input size
arr = [1011, 100, 0, 2, 444, 9288, 8, 1, 1245]

def simple_sort_ascending(arr):
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[i]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            j += 1
        i += 1
simple_sort_ascending(arr)
