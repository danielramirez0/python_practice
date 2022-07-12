from inspect import getfullargspec


class MergeSort():
    def __init__(self) -> None:
        pass

    def merge(self, arr, start, midpoint, end):
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


    def merge_sort(self, arr, start, end):
        if start >= end:
            return
        midpoint = int((start + end) / 2)
        self.merge_sort(arr, start, midpoint)
        self.merge_sort(arr, midpoint + 1, end)
        self.merge(arr, start, midpoint, end)


    def run(self, arr):
        self.merge_sort(arr, 0, len(arr) - 1)


    def run_test(self):
        test_array = [7, 2, 19, 17, 21, 4, 3, 15, 18, 5]
        print(test_array)
        self.merge_sort_(test_array)
        print(test_array)
