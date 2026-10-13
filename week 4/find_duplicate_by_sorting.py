def find_duplicate_by_sorting(arr):

    arr.sort()

    for i in range(len(arr)-1):
        if arr[i] == arr[i+1] :
            return True

    return False





l = ([5,4,9,1,2,4,1],[7,4,5,1,9,4],[7,8,9,4,5,6,1,2,3])

for i in l:
    print(find_duplicate_by_sorting(i))
