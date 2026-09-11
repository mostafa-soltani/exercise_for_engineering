class find_3_NUM:
    def __init__(self,arr) -> None:
        self.arr = arr

    # find smaller from left and store in smaller list of -1 
    def smaller(self):

        smaller = [-1] * len(self.arr)

        min = 0

        for i in range(1,len(self.arr)):
            if self.arr[i] <= self.arr[min]:
                min = i

            else:
                smaller[i] = min

        return smaller

    # find biggest number form right to left and store in greater list of -1
    def greater(self):

        greater = [-1] * len(self.arr)

        max = len(self.arr) - 1

        for i in range(len(self.arr)-2,-1,-1):
            if self.arr[i] >= self.arr[max]:
                max = i
            else:
                greater[i] = max

        return greater
    
    #return the middle number and the smaller and biggest number in list sequence 
    def find(self):

        smaller = self.smaller()
        greater = self.greater()


        for i in range(len(self.arr)):
            if smaller[i] != -1 and greater[i] != -1:
                return [self.arr[smaller[i]],self.arr[i],self.arr[greater[i]]]


arr = [12, 11, 10, 5, 6, 2, 30]

f = find_3_NUM(arr)


print(f.find())