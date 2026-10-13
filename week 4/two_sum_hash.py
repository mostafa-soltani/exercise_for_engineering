

def two_sum_hash(arr,num):

    seen = dict()

    for i in range(len(arr)):
        complete = num - arr[i]

        if complete not in seen:
            seen[arr[i]] = i
        else:
            index = seen[complete]

            return arr[index],arr[i]

    return None

print(two_sum_hash([4, 2, 7, 1], 9))
# (2, 7)

print(two_sum_hash([1, 8, 2, 7], 9))
# (1, 8)

print(two_sum_hash([1, 3, 5], 20))
# None
