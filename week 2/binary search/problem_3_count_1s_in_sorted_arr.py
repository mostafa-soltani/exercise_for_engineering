class count_1s_in_sorted_arr:
    def __init__(self,arr) -> None:
        self.arr = arr

    def count(self):
        count = 0
        for i in range(len(self.arr)):
            if self.arr[i] == 1:
                count += 1

        return count

arr = [1, 1, 1, 1, 1, 1, 1]
f = count_1s_in_sorted_arr(arr)

print(f.count())
