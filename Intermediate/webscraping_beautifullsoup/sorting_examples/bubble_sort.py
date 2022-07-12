# Slow, calc grows exponetially as inputs grow

arr = [1011, 100, 0, 2, 444, 9288, 8, 1, 1245]

def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp


def bubble(arr, length):
    i = length - 1
    while i > 0:
        if arr[i] < arr[i-1]:
            swap(arr, i, i-1)
        i -= 1

def bubble_sort(arr, length):
    i = 0
    while i < length - 1:
        bubble(arr, length)
        i += 1

bubble_sort(arr, len(arr))