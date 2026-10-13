class quick_sort:

    def sort(self,arr):

        if len(arr) <= 1:
            return arr

        pivot = arr[-1]

        left = []
        right = []

        for i in range(len(arr) - 1):
            if arr[i] < pivot:
                left.append(arr[i])

            else:
                right.append(arr[i])

        return quick_sort().sort(left)+[pivot]+quick_sort().sort(right)



ar = [10, 7, 8, 9, 1, 5]

f = quick_sort()

print(f.sort(ar))