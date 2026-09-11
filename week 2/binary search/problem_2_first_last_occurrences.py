
class find_first_last_of_a_sorted_array:
    def __init__(self,arr,x) -> None:
        # getting the arr
        self.arr = arr

        # the number we looking for
        self.x = x

        # the first x we find
        self.first = 0

        # the last x we find
        self.last = 0

        # run the func for find the first x
        self.find_first()

        # run the func for find the lasr x
        self.find_last()
    # the func for find first x
    def find_first(self):
        # initialize the left
        left = 0
        # initialize the right
        right = len(self.arr) -1

        # loop for checking
        while left <= right:
            # the middle number in arr
            mid = left + (right - left) //2
            # check if value of mid is equal to x
            if self.arr[mid] == self.x:
                # if true update the first
                self.first = mid
                # and move to the right half of arr
                right = mid -1
            # check if value of mid is less than x
            elif self.arr[mid] < self.x:
                # if true update the left to use the right half of arr
                left = mid + 1
            # check if value of mid is greater than x
            elif self.arr[mid] > self.x:
                # if true update the right ti use the left half of arr
                right = mid -1

        # if not found update the first to -1
        self.first = -1
    # func to find the last x
    def find_last(self):

        # initialize the left
        left = 0
        # initialize the right
        right = len(self.arr) - 1
        # loop for checking
        while left <= right:
            # the middle number in arr
            mid = left + (right - left) // 2
            # check if value of mid is equal to x
            if self.arr[mid] == self.x:
                # if true update the first
                self.last = mid
                # and move to the right half of arr
                left = mid +1
            # check if value of mid is less than x
            elif self.arr[mid] < self.x:
                # if true update the left to use the right half of arr
                left = mid +1
            # check if value of mid is greater than x
            elif self.arr[mid] > self.x:
                # if true update the right ti use the left half of arr
                right = mid - 1

        # if not found update the first to -1
        self.last = -1

    # use the class
    def find(self):


        return [self.first,self.last]


if __name__ == "__main__":
    arr = [1, 2, 3]
    f = find_first_last_of_a_sorted_array(arr,7)

    print(f.find())
