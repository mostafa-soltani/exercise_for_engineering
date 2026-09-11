
class square_root_num_3:
    def __init__(self,n) -> None:
        # the actual num 
        self.n = n

    def find(self):
        # lowest number for compering
        low = 0
        # highest num that is the n
        high = self.n
        # the number of mid times mid
        prep = 0
        # middle of n
        mid = 1

        try:
            # loop for check
            while low <= high:
                #get the middle num by this furmula
                mid = low + (high - low) // 2
                # get the prep by do mid * mid
                prep = mid * mid

                # check the prep if is lower or equal to n
                if prep <= self.n:
                    # if true update the low
                    low = mid +1
                # check if prep greater of equal to n
                elif prep >= self.n:
                    # if true update the high
                    high = mid -1

            # return mid that is correct
            return mid

        except:
            # if not found or get return -1
            return -1

# use the class 
f = square_root_num_3(13)

# print the result
print(f.find())