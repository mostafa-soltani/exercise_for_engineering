class insertion_sort:

    def sort(self,arr):

        for i in range(1,len(arr)):

            key = arr[i]

            j = i - 1

            while j >= 0 and arr[j] > key:

                arr[j+1] = arr[j]

                j -= 1

            arr[j + 1] = key
            
        return arr

ar = [7, 4, 9, 2, 5, 1]

f = insertion_sort()

print(f.sort(ar))