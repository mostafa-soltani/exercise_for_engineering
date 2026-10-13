class cycle_sort:

    def smaller(self, arr, current):

        count = 0

        for i in range(len(arr)):

            if current > arr[i]:
                count += 1

        # duplicate handling
        while count < len(arr) and arr[count] == current:
            count += 1

        return count


    def test(self, arr):

        for i in range(len(arr)):
            count = self.smaller(arr, arr[i])

            if count != i:
                return False

        return True


    def cycle_sort(self, arr, index):

        count = self.smaller(arr, arr[index])

        displaced = arr[count]

        arr[count] = arr[index]

        while not self.test(arr):

            count = self.smaller(arr, displaced)

            # duplicate handling
            while count < len(arr) and arr[count] == displaced:
                count += 1

            print(count,len(arr))

            current = arr[count]

            arr[count] = displaced

            displaced = current


    def sort(self, arr):

        for i in range(len(arr)):

            count = self.smaller(arr, arr[i])

            if count != i:
                self.cycle_sort(arr, i)

        return arr


if __name__ == "__main__":

    arr = [1, 5, 4, 1, 8, 7]

    f = cycle_sort()

    print(f.sort(arr))