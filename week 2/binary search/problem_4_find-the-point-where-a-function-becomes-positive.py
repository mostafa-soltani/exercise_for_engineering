class find_positive:

    # Monotonically increasing function: as x increases, f(x) increases
    def f(self, x):
        return x * 2 - 10

    def find_range(self):
        last_num = 0
        current_num = 1

        # Keep doubling until f(x) becomes positive
        while self.f(current_num) <= 0:

            # Save the previous value to create the lower boundary
            last_num = current_num

            # Double the current value to search farther
            current_num = current_num * 2

        # Return the range where the first positive value must exist
        return last_num, current_num

    def binary(self):
        # Get the lower and upper boundaries for Binary Search
        low, high = self.find_range()

        print(low, high)

        # Binary Search inside the discovered range
        while low <= high:

            # Find the middle index/value of the current range
            mid = low + (high - low) // 2

            # Check if mid is the first positive value
            if (self.f(mid) > 0 and
                    (mid == low or self.f(mid - 1) <= 0)):
                return mid

            # If mid is not positive, search the right half
            if self.f(mid) <= 0:
                low = mid + 1

            # If mid is positive, search the left half for an earlier positive
            else:
                high = mid - 1


f = find_positive()

print(f.binary())