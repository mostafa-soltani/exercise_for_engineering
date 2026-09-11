

class equilibrium_index:
    def __init__(self,arr) -> None:
        self.arr = arr

    def sum(self):
        sum = 0
        for i in range(len(self.arr)):
            sum += self.arr[i]

        return sum

    def start(self):
        left = 0
        right = 0

        total = self.sum()
        for i in range(len(self.arr)):
            current = self.arr[i]
            right = total - left - current

            if left == right:
                return i
            left += current
        return -1

arr = [1, 2, 0, 3]


f = equilibrium_index(arr)

print(f.start())