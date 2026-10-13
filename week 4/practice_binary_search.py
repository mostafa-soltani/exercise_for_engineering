def binary_search(arr,num):

    left = 0

    right = len(arr)-1


    while left <= right:
        mid = (right+left) // 2

        if arr[mid] == num:
            return mid

        elif arr[mid] < num:
            left = mid + 1

        elif arr[mid] > num:
            right = mid - 1


    return -1


print(binary_search([2, 6, 10, 14, 18, 22, 26, 30, 34], 26))  # 6
print(binary_search([2, 6, 10, 14, 18, 22, 26, 30, 34], 2))   # 0
print(binary_search([2, 6, 10, 14, 18, 22, 26, 30, 34], 35))  # -1
print(binary_search([], 5))                                   # -1