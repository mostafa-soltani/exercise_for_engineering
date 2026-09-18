class selection_sort:

    def sort(self,arr):

        for i in range(len(arr)):

            min_index = i
            current = arr[i]
            for j in range(i+1,len(arr)):

                if arr[j] < arr[min_index]:
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr



arr = [7,4,9,2,5,1]

f = selection_sort()

print(f.sort(arr))