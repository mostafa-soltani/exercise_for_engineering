def linear_search(arr,num):

    for index in range(len(arr)):
        if arr[index] == num:
            return index
        else:
            continue

    return -1



print(linear_search([9, 4, 12, 7], 12))  # 2
print(linear_search([9, 4, 12, 7], 5))   # -1
print(linear_search([], 5))              # -1

