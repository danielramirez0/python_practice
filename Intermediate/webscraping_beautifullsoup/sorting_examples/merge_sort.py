
test_array = [7, 2, 19, 17, 21, 4, 3, 15, 18, 5]


def combine(arr, start, midpoint, end):
    buffer = [0] * len(arr) # used to copy the arary to not add complexity of in place edits
    k = start
    while k <= end:
        buffer[k] = arr[k]
        k = k + 1

    i = start
    j = midpoint + 1
    k = start

    while i <= midpoint and j <= end:
        if buffer[i] <= buffer[j]:
            arr[k] = buffer[i]
            i += 1
        else:
            arr[k] = buffer[j]
            j += 1
        k += 1

    while i <= midpoint:
        arr[k] = buffer[i]
        i += 1
        k += 1

    while j <= end:
        arr[k] = buffer[j]
        j += 1
        k += 1


def merge_sort(arr, start, end):
    if start >= end:
        return
    midpoint = int((start + end) / 2)
    merge_sort(arr, start, midpoint)
    merge_sort(arr, midpoint + 1, end)
    combine(arr, start, midpoint, end)


def merge_wrapper(arr, length):
    merge_sort(arr, 0, length - 1)


print(test_array)
merge_wrapper(test_array, len(test_array))
print(test_array)
