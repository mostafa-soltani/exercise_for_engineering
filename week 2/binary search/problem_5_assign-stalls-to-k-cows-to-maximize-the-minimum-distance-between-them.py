
class cow_place:
    def check(self,arr,k,dist):
        # place the first cow on first index
        cnt = 1
        prev = arr[0]

        for i in range(1,len(arr)):

            # if the current stall is at least dist away 
            # from the prev one place the cow there

            if arr[i] - prev >= dist:
                prev = arr[i]
                cnt += 1

        # check and return a bool value to if the cows is the right amont 
        return cnt >= k



    def aggrasiveCow(self,arr,k):

        # sort the arr first to do binary
        arr.sort()

        result = 0


        low = 0
        high = arr[-1] - arr[0]

        while low <= high:  
            # detrmine the mid 
            mid = low + (high - low) //2

            # check if the arr is good enough to to fit the cows or not 
            if self.check(arr,k,mid):
                result = mid
                low = mid +1
            # if not do the left side of arr
            else:
                high = mid -1 
        # the result is the mid distance beetwen cows and when its good return it 
        return result


if __name__ == "__main__":
    arr = [1, 2, 4, 8, 9]
    k = 3

    ans = cow_place()

    print(ans.aggrasiveCow(arr,k))

