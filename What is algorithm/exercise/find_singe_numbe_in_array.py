arr = [2, 2, 5, 20, 20, 30, 30]

class find_single:
    def __init__(self,arr) -> None:
        self.arr = arr
        self.seen = {}
        self.count = 1

    def find(self):
        for index in range(len(arr)):
            if arr[index] not in self.seen:
                self.seen[arr[index]] = self.count

            else:
                self.seen[arr[index]] = self.count +1

        for item,count in self.seen.items():
            if count == 1:
                return item



f = find_single(arr)

print(f.find())