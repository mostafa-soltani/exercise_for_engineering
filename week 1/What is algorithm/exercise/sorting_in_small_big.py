


class sorting_small_big:
    def __init__(self,arr):
        self.arr = arr
        self.new_arr = []
        pass

    def algorithm(self,arr):
        for index in range(len(arr)):
        
            previous = arr[index - 1]
            current = arr[index]
        
            if index != 0:
                if index % 2 == 1:
                    if previous <= current:
                        continue
                    else:
                        arr[index -1] = current
                        arr[index] = previous
        
        
                if index % 2 == 0:
                    if previous >= current:
                        continue
                    else:
                        arr[index -1] = current
                        arr[index] = previous

        return arr

    def sort(self):
        for arr in self.arr:
            arr2 = self.algorithm(arr)
            self.new_arr.append(arr2)
        return self.new_arr


arr = [[5, 3, 8, 2, 7, 4],[1, 2, 3, 4, 5, 6],[6, 5, 4, 3, 2, 1],[4,8,1,5,9,9,8],[1,3,2,5,4,8,2,9]]
arr2 = [1, 2, 3, 4, 5, 6]
arr3 = [6, 5, 4, 3, 2, 1]
arr4 = [4,8,1,5,9,9,8]

sorting = sorting_small_big(arr)

print(sorting.sort())