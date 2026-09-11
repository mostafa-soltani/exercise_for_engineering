arr = [8, 2, 4, 5, 3, 7, 1]



class find_missing_num:
    def __init__(self,arr) -> None:
        self.arr = arr
        self.seen = seen = {}


    def find(self):
    
        for index in range(len(self.arr)):
            self.seen[self.arr[index]] = True

        for value in range(1,len(self.arr)+2):

            if value not in self.seen:
                return value
            else:
                continue


f = find_missing_num(arr)

print(f.find())