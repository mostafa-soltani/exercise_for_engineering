def example(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1):
            count += 1
            print(arr[i], arr[j],count)


arr2 = [1,2,3,4,5,6]

example(arr2)


'''
1
2
3
4
n2 + n2 = n4
'''