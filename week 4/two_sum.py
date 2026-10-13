def two_sum(arr,num):

    left = 0

    right = len(arr)-1

    while left < right:

        if arr[left] + arr[right] == num:
            return arr[left] , arr[right]

        elif arr[left] + arr[right] > num:
            right -=1

        elif arr[left] + arr[right] < num:

            left += 1


    return None


print(two_sum([1, 2, 4, 6, 8, 11], 10))
# (2, 8)

print(two_sum([1, 3, 5, 7], 20))
# None