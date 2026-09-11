class split_array_into_3:
    def __init__(self,arr) -> None:
        self.arr = arr

    def summ(self):
        sum = 0
        for index in range(len(self.arr)):
            sum += self.arr[index]

        return sum

    def split(self):
        point = []
        total = self.summ()
        current = 0
        c_sum = 0
        print(total)

        if not total // 3 != 0:

            point = [-1,-1]
            return point

        target = total / 3


        for index in range(len(self.arr)):
            current = self.arr[index]

            c_sum += current

            if c_sum == target:
                point.append(index)
                c_sum = 0
                if len(point) == 2:
                    return point



arr = [1, -1, 1, -1, 1, -1, 1, -1]

f = split_array_into_3(arr)

print(f.split())

        